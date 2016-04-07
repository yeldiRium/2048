class GameNotInitializedError(Exception):
    pass


class GameLostError(Exception):
    pass


class InvalidActionError(Exception):
    pass


class NoEmptyContainerError(Exception):
    pass


class MoveNotAllowedError(Exception):
    pass


class FusionNotAllowedError(Exception):
    pass
