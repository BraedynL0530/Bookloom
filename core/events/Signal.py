import asyncio

class Signal:
    def __init__(self):
        self.listners = []
        
    def connect(self, func):
        self.listners.append(func)
        return lambda: self.disconnect(func)

    def disconnect(self, func):
        self.listners.remove(func)

    def emit(self, *args, **kwargs):
        for func in self.listners:
            func(*args, **kwargs)

    async def wait_for_next(self, timeout: float = None): #wait untill function is called again or after timeout(thread blocking listener)
        future = asyncio.get_event_loop().create_future()

        def internal_callback(*args, **kwargs):
            if not future.done():
                future.set_result(args,kwargs)

        disconnect_func = self.connect(internal_callback)

        try:
            if timeout is not None:
                return await asyncio.wait_for(future, timeout=timeout)
            else:
                return await future

        finally:
            disconnect_func()



    async def asyncio_wait_for_complete_or_timeout(fut, timeout):
        return await asyncio.wait_for(fut, timeout=timeout)