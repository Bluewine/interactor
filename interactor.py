class Context(object):

    @classmethod
    def build(cls, **context):

        return cls(**context)

    def __init__(self, **context):

        _ = [setattr(self, key, context[key]) for key in context]


class Interactor(object):

    @classmethod
    def call(cls, **context):

        instance = cls(**context)
        instance.run()
        return instance.context

    def __init__(self, **context):

        self.context = Context.build(**context)

    def run(self):

        raise NotImplementedError()
