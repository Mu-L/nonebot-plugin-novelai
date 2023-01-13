import hashlib
from pathlib import Path

import aiofiles

from ..config import config

path = Path("data/novelai/output").resolve()


async def save_img(request, img_bytes: bytes, extra: str = "unknown"):
    # 存储图片
    if config.novelai_save:
        path_ = path / extra
        path_.mkdir(parents=True, exist_ok=True)
        hash = hashlib.md5(img_bytes).hexdigest()
        file = (path_ / hash).resolve()
        async with aiofiles.open(str(file) + ".jpg", "wb") as f:
            await f.write(img_bytes)
        if config.novelai_debug:
            async with aiofiles.open(str(file) + ".txt", "w") as f:
                await f.write(repr(request))
