# Kuest Builder Signing SDK

<a href='https://pypi.org/project/kuest-py-builder-signing-sdk'>
    <img src='https://img.shields.io/pypi/v/kuest-py-builder-signing-sdk.svg' alt='PyPI'/>
</a>

Python SDK for Kuest builder authentication and signing.

## Installation

```bash
pip install kuest-py-builder-signing-sdk
```

## Usage

```python
from py_builder_signing_sdk import BuilderConfig, BuilderApiKeyCreds, RemoteBuilderConfig

# Local signing
creds = BuilderApiKeyCreds(
    key="your-api-key",
    secret="your-secret", 
    passphrase="your-passphrase"
)
config = BuilderConfig(local_builder_creds=creds)

# Remote signing
remote_config = RemoteBuilderConfig(
    url="http://localhost:3000/sign",
    token="your-auth-token"  # optional
)
config = BuilderConfig(remote_builder_config=remote_config)

# Generate signed headers
headers = config.generate_builder_headers("POST", "/order", '{"data": "example"}')
```
