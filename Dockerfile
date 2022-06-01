FROM docker-registry.bimdata.io/public/python-poetry:3.9 as builder-base

FROM docker-registry.bimdata.io/public/python-django:3.9

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Disable Django stuff
ENV COLLECT_STATIC 0
ENV APPLY_MIGRATION 0
