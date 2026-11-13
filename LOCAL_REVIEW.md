# Local Deconstruction and Minor Refactor

Source repository: https://github.com/worldonlyu/Google_AI_Pro_2Year_ZeroCost_Auto

Baseline commit: 1fb2e16711d842ec8fe7db44357a0cf1f1633172

## Modules and call relationships

| File | Responsibility |
| --- | --- |
| `templates/index.html` | Single-page console; polls status every 1.5 seconds and submits config and task requests |
| `app.py` | FastAPI routes, config read/write, in-memory task queue, logs, manual browser entry point |
| `automation_engine.py` | Browser location, proxy bridge, auth helpers, Playwright flow, and screenshots |
| `config.json` | Local JSON storage for config and account state |
| Two `.bat` files | Install dependencies and start the service on local port 8765 |

Data flow: web page → FastAPI routes → JSON config / in-memory tasks → automation engine → state callback → JSON config → status polling → web page.

## Changes in this round

`get_state()` changed from copying the full account dict to an explicit whitelist of display fields. Passwords, recovery emails, TOTP secrets and dynamic codes, per-account proxies, and any fields added in the future but not whitelisted are no longer returned in the account list. A new boolean field `has_totp` indicates whether two-step verification is configured.

The front end was updated to match: credential display and the whole-account copy button were removed, while the verification-method label was kept. Config form back-fill, save semantics, routes, the automation engine, and dependencies are unchanged. It was not split into multiple services and no new framework was added.

## Verification and limits

Run `python check_state.py app.py --require-redacted` to verify the actual state-handling function offline. It uses fictitious accounts, does not import the automation engine, and does not sign in, bind a card, or start a subscription. This check covers the serialization boundary only; it is not equivalent to browser-side or real end-to-end subscription verification.

Found but not addressed this round: the config and top-level state response still contain the payment card and proxy template; run logs may contain dynamic verification codes; some account fields go straight into HTML; JSON writes lack atomic replacement; the batch-running flag is set only inside the async task, leaving a window for duplicate scheduling; and the Windows GBK console may be unable to print emoji.

This round only reduces credential exposure in the account list; it does not guarantee that all responses, logs, or screenshots are free of sensitive information. The README's claims of zero cost and two-year benefits are upstream project claims and have not been verified. Its promotion-stacking or payment flows were not executed.
</Content>
