# shazeus Rose Fork Notes

This fork keeps Rose's upstream runtime behavior intact and only carries fork-local packaging, documentation, and visible project-link customization.

## Fork-Specific Changes

- GitHub-facing links in the README, installer metadata, and in-client settings panel point to `shazeus/Rose`.
- The launcher updater now checks `shazeus/Rose` releases by default.
- The updater release source can be overridden with `ROSE_RELEASE_REPO` or `ROSE_RELEASE_API` for testing/custom builds.
- Upstream support/community links are left unchanged unless this fork starts maintaining its own support channel.
- Runtime injection, loader, and asset-processing behavior are intentionally untouched by this fork customization pass.

## Maintenance Rules

- Keep fork-only branding changes separate from runtime logic changes.
- Prefer small commits that are easy to compare against upstream.
- Re-check upstream changes before editing League Client integration code.
