FROM ubuntu:22.04

# Install the standard Kerberos server and utilities headlessly
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y krb5-kdc krb5-admin-server && rm -rf /var/lib/apt/lists/*

# Add a simple initialization script that starts the Kerberos service
RUN echo '#!/bin/sh\n\
if [ ! -f /var/kerberos/krb5kdc/principal ]; then\n\
    kdb5_util create -s -P Password123\n\
    kadmin.local -q "addprinc -pw Password123 admin/admin"\n\
fi\n\
krb5kdc -n' > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
