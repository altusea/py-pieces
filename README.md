# py-pieces

Python 代码片段集合 —— 包含算法实现、库使用示例、以及一些有趣的编程练习。

## 项目结构

```
py-pieces/
├── examples/          # 第三方库使用示例
│   ├── anyio_test.py  # anyio + trio 异步运行时
│   ├── async_demo.py  # asyncio 基础示例
│   ├── collections_demo.py  # collections 模块
│   ├── discryptor_demo.py   # Python 描述器协议
│   ├── enum_demo.py   # enum.Flag 枚举类型
│   ├── polars_test.py # Polars 数据帧处理
│   └── serde_test.py  # orjson 序列化
├── snippets/          # 算法与编程练习
│   ├── blossom_algo.py # Edmonds' Blossom 最大匹配算法
│   ├── copy.py        # 自定义迭代器示例
│   ├── kata.py        # Codewars Kata 练习集
│   ├── prime.py       # 素数生成器
│   └── rhythmic.py    # 数字韵律评分系统
├── src/               # Python 包
│   └── ulib/          # 工具库
│       └── utils/
│           └── model.py
├── .github/
│   └── dependabot.yml # 依赖更新配置
├── pyproject.toml     # 项目配置
├── ruff.toml          # Ruff 配置
└── uv.lock            # 依赖锁文件
```

## 环境要求

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) —— 快速的 Python 包管理器

## 安装依赖

```bash
# 安装项目依赖（包含开发依赖）
uv sync --all-groups
```

## 运行示例

```bash
# 运行任意示例脚本
uv run python examples/polars_test.py
uv run python snippets/blossom_algo.py
```

## 开发工具

- **Ruff** —— 快速的 Python 代码检查器
- **ty** —— 类型检查工具

```bash
# 代码检查
uv run ruff check .

# 自动修复
uv run ruff fix .

# 类型检查
uv run ty check
```

## 目录说明

### examples/

包含各种第三方库的使用示例：

- **anyio_test.py** —— anyio 异步库与 trio 运行时的结合使用
- **async_demo.py** —— asyncio 协程基础示例
- **collections_demo.py** —— collections.defaultdict 的行为演示
- **discryptor_demo.py** —— Python 描述器协议的完整实现，包括验证器模式
- **enum_demo.py** —— enum.Flag 位标志枚举的日期转换示例
- **polars_test.py** —— Polars 高性能数据帧处理库入门
- **serde_test.py** —— orjson 序列化与 dataclass 的配合

### snippets/

包含算法实现和编程练习：

- **blossom_algo.py** —— Edmonds' Blossom 算法，用于一般无向图的最大匹配
- **copy.py** —— 自定义反向迭代器的实现
- **kata.py** —— Codewars 编程练习合集，包括：
  - 简单汇编语言解释器
  - 表达式计算器（手写递归下降解析）
  - 错位排列计算
  - 骑士最短路径（BFS）
  - 罗马数字转换
- **prime.py** —— 素数判断与特殊素数生成
- **rhythmic.py** —— 基于汉语声调的数字韵律评分系统，寻找最具"抑扬顿挫"感的六位数
