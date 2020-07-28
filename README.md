# Prometheus Markdown Docs

Ever wanted to generate docs about your Prometheus metrics programmatically? If so, this script is for you! Just pass it the url of a Prometheus metrics endpoint and it will generate a markdown list like so:

```bash
╔ ☕️  gene:~/repos/prometheus-markdown-docs
╚ᐅ ./parse-prom-endpoint.py 'http://10.221.68.74:4567/prometheus'
- `vmpooler_checkout_empty` (counter): Pool checkout counts checkout failed - no machine
- `vmpooler_checkout_invalid` (counter): Pool checkout counts checkout failed - invalid template
- `vmpooler_checkout_nonresponsive` (counter): Pool checkout counts checkout failed - non responsive machine
- `vmpooler_checkout_success` (counter): Pool checkout counts successful checkout
- `vmpooler_config_invalid` (counter): vmpooler pool configuration request Invalid
- `vmpooler_delete_failed` (counter): Delete machine failed
- `vmpooler_delete_success` (counter): Delete machine succeeded
- `vmpooler_http_exceptions` (counter): The total number of exceptions raised by the Rack application.
- `vmpooler_http_request_duration_seconds` (histogram): The HTTP response duration of the Rack application.
- `vmpooler_http_requests_vm` (counter): Total number of HTTP request/sub-operations handled by the Rack application under the /vm endpoint
- `vmpooler_http_requests` (counter): The total number of HTTP requests handled by the Rack application.
- `vmpooler_ondemandrequest_fail_invalid` (counter): Ondemand request failure invalid poolname
- `vmpooler_ondemandrequest_fail_toomanyrequests` (counter): Ondemand request failure too many requests
- `vmpooler_ondemandrequest_generate_duplicaterequests` (counter): Ondemand request failed duplicate request
- `vmpooler_ondemandrequest_generate_success` (counter): Ondemand request succeeded
- `vmpooler_poolreset_invalid` (counter): Pool reset counter Invalid Pool
```
