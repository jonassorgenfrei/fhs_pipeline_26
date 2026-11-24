class Shot:
    def __init__(
        self, name: str, status: str = "ready", frames: list[int] = [1001, 1050]
    ):
        self.name = name
        self.status = status
        self.frames = frames

    def all_frames(self) -> list[int]:
        return list(range(self.frames[0], self.frames[1] + 1))

    def label(self):
        return f"{self.name} ({self.status})"
