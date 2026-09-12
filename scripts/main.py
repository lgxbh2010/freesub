#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
兼容入口 (compat launcher)
==========================

本 fork 的 GitHub Actions 工作流 `.github/workflows/update.yml` 仍调用
`python scripts/main.py`（v1 入口）；而上游 v2 把测活引擎整体迁移到了
`scripts/main_v2.py`。

为了避免改动 `.github/workflows/` 下的文件（本机 gh token 无 `workflow`
作用域，任何对工作流文件的推送都会被 GitHub 拒绝），这里保留一个极薄的
转发层：直接以 __main__ 方式执行 main_v2.py。

好处：`scripts/main_v2.py` 与上游保持逐字节一致，后续同步上游时不会产生
额外冲突；本文件是唯一的本地增量。
"""

import os
import runpy
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_TARGET = os.path.join(_HERE, "main_v2.py")

if not os.path.exists(_TARGET):
    sys.exit(f"[!] 找不到 v2 引擎: {_TARGET}")

sys.argv = [_TARGET] + sys.argv[1:]
runpy.run_path(_TARGET, run_name="__main__")
