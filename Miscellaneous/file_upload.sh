#!/bin/sh
export PRTCL="https";
export HOST="www.sapconinstruments.com";

export ERP_KEY="172b5f5d5ff8f21";
export ERP_SCT="c5612a07b3082ed";

export DOCTYPE="IOT Raw Log";
export DOCID=$1;

export THEFILE="Vital_fig.png";
export FILEDATA=$(base64 -w 0 ${THEFILE});

sudo curl -s -X POST "${PRTCL}://${HOST}/api/method/frappe.client.attach_file" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -H "Authorization: token ${ERP_KEY}:${ERP_SCT}" \
        --data-urlencode "filename=${THEFILE}" \
        --data-urlencode "filedata=${FILEDATA}" \
        --data-urlencode "doctype=${DOCTYPE}" \
        --data-urlencode "docname=${DOCID}" \
        --data-urlencode "is_private=1" \
        --data-urlencode "decode_base64=1" \
  | jq -r .;

