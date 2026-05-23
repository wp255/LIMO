# Format Checking Rules

Format checking verifies whether the candidate JSON is structurally complete and machine-readable.

## Required Fields

The candidate JSON must contain:
- `serviceType`
- `sliceType`
- `latency`
- `throughput`
- `region`
- `reliability`
- `priority`
- `time`

## Missing Field Errors

Report missing required fields exactly and concisely.

Examples:
- Missing `priority`: `Missing required field 'priority'.`
- Missing `time`: `Missing required field 'time'.`
- Missing `region`: `Missing required field 'region'.`

## Field Format Rules

### serviceType
Must be one of:
- `URLLC`
- `eMBB`
- `mMTC`

### sliceType
Must be a string and should contain a service prefix and scenario name.

### latency
Must be a string containing a number and `ms`.
Valid examples:
- `"<2ms"`
- `"<80ms"`
- `"145ms"`

### throughput
Must be a string ending with `Mbps`.
Invalid examples:
- `325.0`
- `50.0`
- `0.29`

Error pattern:
`Field 'throughput' should be a string with 'Mbps', but got '<value>'.`

### reliability
Must be a string ending with `%`.
Invalid examples:
- `"99.910"`
- `"99.68"`
- `"98"`
- `99.971`

Error pattern:
`Field 'reliability' should be a string ending with '%', but got '<value>'.`

### priority
Must be a string from `"1"` to `"5"`.

### time
Should be a string containing a date, preferably `YYYY-MM-DD`.

## Important Distinction

Format checking should not judge whether QoS values are reasonable. For example:
- `"latency": "<80ms"` is format-valid, even if it is semantically too high for eMBB or URLLC.
- `"throughput": "500Mbps"` is format-valid, even if it is semantically wrong for mMTC.
