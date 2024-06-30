from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomStaticFilesStorage(CompressedManifestStaticFilesStorage):
    def url(self, name, force=False):
        try:
            return super().url(name, force=force)
        except ValueError:
            return None
