- 如果你希望改用 json 储存字符映射, 请前往 <a href="https://github.com/gtj1/symbol_assist/tree/symbol_json">symbol_json 分支</a>
- 如果你希望直接运行可执行文件而非通过 `python`, 请前往 <a href="https://github.com/gtj1/symbol_assist/tree/symbol_ahk">symbol_ahk 分支</a> (此版本基于Auto HotKey)
- 提示：main 分支采用硬编码储存字符映射, 此版本是旧的版本

# 关于

本程序受到证明语言 `Lean` 中符号输入方式的的启发, 旨在帮助日常生活中的数学符号输入, 例如使用 `\a` 轻松地输入 `α`. 程序输入得到的是 `unicode` 字符, 需要注意的是这与 `TeX` 渲染得到公式的原理不同, `unicode` 字符并不能代替 `TeX` 公式渲染的任务, 但是可以极大地方便需要输入数学符号的交流.

在运行程序时请确保您切换大小写使用的是 `Shift` 而不是 `Caps Lock`, 否则可能不能正常输入包含大写字符的符号.

程序尚在开发中, 欢迎您的参与与建议.

# 预备工作

这是一个简单的符号输入辅助脚本, 为了运行它, 你的电脑上应该安装了 `python3`, 且安装了两个 `python` 库：`pynput, keyboard`, 如果你还没有安装, 使用如下命令通过命令行安装：

```bash
pip install pynput keyboard
```

或者如果你使用 anaconda：

```
conda install pynput keyboard
```

# 文件说明

`main.py` 是需要运行的脚本, `symbols.py` 是符号表, 包含若干预定义的符号, 运行时你可以使用任何的集成 IDE 运行或者在命令行中使用 `python main.py` 以运行.  在此之后只需要保持程序在后台运行, 然后在网页、聊天界面的输入框、记事本等任何界面输入文字即可.

# 使用方法

在脚本运行的状态下, 输入字符的代码, 然后按下空格, 就可以获得要输入的内容, 例如, 要输入 `∀n≥3, a b c∈ℕ₊, aⁿ+bⁿ≠cⁿ`

需要按下的按键顺序是（符号列表在下文会介绍）

`\al n\ge 3, a b c\in \N \_+ , a\^n +b\^n \ne c\^n`

当按下 `\al` 后输入空格时, `\al` 会自动变为 `∀`. 当输入 `\ge` 后按下空格时, `\ge` 会自动变为 `≥`, 如此下去, 输入整条式子后, 你的输入框内将会包含

````
∀n≥3, a b c∈ℕ₊, aⁿ+bⁿ≠cⁿ
````

又或者你可以使用数学字体 $n,a, b, c$, 即输入

```
\al \Min \ge 3, \Mia \Mib \Mic \in \N \_+ , \Mia \^n +\Mib \^n \ne \Mic \^n
```

这将会得到

```
∀𝑛≥3, 𝑎 𝑏 𝑐∈ℕ₊, 𝑎ⁿ+𝑏ⁿ≠𝑐ⁿ
```

所以你只需要记住你要打的符号对应的代码（或称为转义字符）, 然后输入即可, 每个转义字符以 `\` 开头, 如果你只希望输入 `\` 而不希望其被作为转义字符, 请连续敲击两次 `\`. 例如如果你希望输入字符串 `C:\Users` 并且不希望在输入的过程中由于转义字符遇到麻烦, 在输入 `\` 时应该输入两次 `\`, 即输入 `C:\\Users`. 常用的符号列表如下：

#### 上下标：

使用 `\^` 来输入上标, `\_` 来输入下标, 例如 `\^n` 后按下空格可以输入 `ⁿ`, 又如 `\_1` 后按下空格可以得到 `₁`, 需要注意的是一些字母的上下标存在缺失, 可能不能得到正常结果, 这些字母包括上标的字母 `Q, W, X, Y, Z, q` 、下标的所有大写字母和小写字母 `b, c, d, f, g, q, y, z`. 除去这些字母外, 其它的字母和全部的数字都可以用此种方法输入. 暂时不支持 `\_12` 输入 `₁₂`, 如果需要输入这样的下标需要通过 `\_1 \_2 ` 分别得到.

特别地, 考虑到常用数字作为下标, 数字下标时可以省去 `_`, 即可以使用 `x\1` 来输入 `x₁`, 而无需使用 `x\_1`. 此外, 考虑到倒数较为常用, 倒数可以直接使用 `\-`, 无需输入 `\^- \^1 `.

## 字体：

可以输入带有字体的英文字母, 这一段中使用 `X` 表示一个字母, 使用时请换成你需要的字母, 转换关系如下

| 符号   | 说明                               | 效果示例 |
| ------ | ---------------------------------- | -------- |
| `\bbX` | 黑板体                             | `ℝ`      |
| `\bfX` | 黑体                               | `𝐯`      |
| `\itX` | 无衬线斜体                         | `𝘢`      |
| `\MiX` | 数学斜体<br />(Math italic)        | `𝑥`      |
| `\McX` | 数学书法体<br />(Math calligraphy) | `𝒞`      |
| `\MfX` | 哥特体<br />(Math fraktur)         | `𝔪`      |

需要注意的是, 由于 Unicode 中不含有数学斜体字符 $h$, `\Mih` 打出的字符实际上是无衬线的斜体 `𝘩`, 其它的字符都可以正常打出.

符号表中为常用的几个字母黑板体提供了缩写：`𝔸, ℂ, 𝔽, ℍ, 𝕂, ℚ, ℝ`  分别可以通过 `\A, \C, \F, \H, \K, \Q, \R` 打出.

## 希腊字母

可以方便地打出希腊字母, 使用方法是在反斜杠 `\` 后加字母的英语名称, 例如输入 `\alpha` 后按下空格可以得到 `α`, 输入 `\Lambda` 后按下空格可以得到 `Λ`. 希腊字母表可以方便地在互联网上查到, 您可以前往 [希腊字母_百度百科 (baidu.com)](https://baike.baidu.com/item/希腊字母/4428067) 查询, 此处不再列出.

符号表中为较为常用的字母提供了缩写：`Γ, Π, Σ, α, β, χ, γ, ε, γ, κ, μ, σ, ζ`​ 分别可以方便地使用 `\G, \P, \S, \a, \b, \c, \e, \g, \k, \m, \s, \z` 打出.

## 箭头

（逗号隔开表示多种输入方式均可, 得到的结果相同, 下同）

| 代码                     | 字符 | 代码                     | 字符 | 代码                    | 字符 |
| ------------------------ | ---- | ------------------------ | ---- | ----------------------- | ---- |
| `\l`, `\leftarrow`       | `←`  | `\ul`, `\upleftarrow`    | `↖`  | `\Leftarrow`            | `⇐`  |
| `\r`, `\rightarrow`      | `→`  | `\ur`, `\uprightarrow`   | `↗`  | `\Ri`, `\Rightarrow`    | `⇒`  |
| `\u`, `\uparrow`         | `↑`  | `\dl`, `\downleftarrow`  | `↙`  | `\bi`, `Leftrightarrow` | `⇔`  |
| `\d`, `\downarrow`       | `↓`  | `\dr`, `\downrightarrow` | `↘`  | `\mapsto`               | `↦`  |
| `\lr`, `\leftrightarrow` | `↔`  | `\ud`, `\updownarrow`    | `↕`  | `\hookrightarrow`       | `↪`  |

## 分数

支持的分数包括 `½, ⅓, ⅔, ¼, ¾, ⅕, ⅖, ⅗, ⅘, ⅙, ⅛, ⅜, ⅝, ⅞`, 输入的格式为

`\fracxy`, 例如 `\frac25` 后按下空格以输入 `⅖`. 由于 `unicode` 字符中不包含其它分数, 所以仅支持这些分数.

## 逻辑、关系和运算符

| 代码                      | 字符 | 代码                      | 字符 |
| ------------------------- | ---- | ------------------------- | ---- |
| `\pm`                     | `±`  | `\le`                     | `≤`  |
| `\x`, `\times`, `\cross`  | `×`  | `\gg`                     | `≫`  |
| `\div`                    | `÷`  | `\ll`                     | `≪`  |
| `\.`                      | `·`  | `\oplus`                  | `⊕`  |
| `\o`, `\circ`, `\comp`    | `∘`  | `\ox`, `\ot`, `\otimes`   | `⊗`  |
| `\i`, `\ca`,`\cap`        | `∩`  | `\bx`, `\boxtimes`        | `⊠`  |
| `\un`, `\cup`             | `∪`  | `\is`, `\cong`            | `≅`  |
| `\in, \me`                | `∈`  | `\~`, `\sim`              | `∼`  |
| `\ss`, `\su`, `\sube`     | `⊆`  | `\:=`                     | `≔`  |
| `\v`, `\and`, `\wedge`    | `∧`  | `\al`, `\fo`, `\forall`   | `∀`  |
| `\or, \vee`               | `∨`  | `\ex`, `\exist`           | `∃`  |
| `\n`, `\no`, `\not`, `\neg` | `¬`  | `\nexist`                 | `∄`  |
| `\=`, `\ne`               | `≠`  | `\|`, `\dv`, `\mi`, `\mid` | `∣`  |
| `\ge`                     | `≥`  | `\nm`, `\nmid`            | `∤`  |

## 微积分

| 代码              | 字符 | 代码              | 字符 |
| ----------------- | ---- | ----------------- | ---- |
| `\int`            | `∫`  | `\oint`           | `∮`  |
| `\iint`           | `∬`  | `\oiint`          | `∯`  |
| `\iiint`          | `∭`  | `\oiiint`         | `∰`  |
| `\nabla`, `\grad` | `∇`  | `\pd`, `\partial` | `∂`  |

 ## 其它

| 代码             | 字符 | 代码                    | 字符 |
| ---------------- | ---- | ----------------------- | ---- |
| `\infty`         | `∞`  | `\cd`, `\do`, `\cdot`   | `⬝`  |
| `\<`,`\langle`   | `⟨`  | `\cdots`                | `⋯`  |
| `\>`, `\rangle`  | `⟩`  | `\vdots`                | `⋮`  |
| `\lc`, `\lceil`  | `⌈`  | `\ddots`                | `⋱`  |
| `\rc`, `\rceil`  | `⌉`  | `\sqrt`                 | `√`  |
| `\lf`, `\lfloor` | `⌊`  | `\cbrt`                 | `∛`  |
| `\rf`, `\rfloor` | `⌋`  | `\!`                    | `¡`  |
| `\da`            | `†`  | `\#`                    | `♯`  |
| `\el`            | `ℓ`  | `\&`                    | `⅋`  |
| `\w`             | `℘`  | `\?`                    | `¿`  |
| `\Re`            | `ℜ`  | `\*`, `\st`, `\star`    | `⋆`  |
| `\Im`            | `ℑ`  | `\ld`                   | `“`  |
| `\hb`, `\hbar`   | `ℏ`  | `\rd`                   | `”`  |
| `\ve`            | `ě`  | `\sq`, `\square`        | `◾`  |
| `\ce`            | `ȩ`  | `\pa`, `\parallelogram` | `▰`  |
| `\ae`            | `æ`  | `\triangle`             | `▵`  |
| `\y`             | `¥`  | `\q`, `\qe`, `\qed`     | `∎`  |
| `\eu`            | `€`  | `\di`, `\diamond`       | `◆`  |
| `\po`            | `£`  | `\Sm`, `\Smile`         | `☺`  |
| `\ru`            | `₽`  | `\Fr`, `\Frowny`        | `☹`  |

# 高级设置

如果您希望添加自己的符号, 请按照 `python` 的字典格式添加, 并使用搜索功能提前确保没有符号的重复（例如如果你希望重定义符号 `\P` 为 `Ψ`, 您需要在 `symbols.py` 中查找 `"\\P":` 这一项并将对应的内容替换为 `"Ψ"`

# Q&A

**Q1.** 为什么运行后 `Ctrl+C` 无法关闭?

**A1.** 直接点击 × 强制关闭终端就好.

**Q2.** 当在某个位置插入字符时不能得到预期的结果, 例如, 为什么在 `\u` 中插入字母 `m` 后没有得到 `μ`, 又比如, 为什么在文本框中已经有 `\m` 时输入 `u` 不会得到 `μ`.

**A2.** 程序依靠检测输入的字符运行, 当输入被打断或者没有按照顺序输入时是没有办法正确将转义字符替换为 `unicode` 数学符号的, 如果遇到类似这种情况请删除已有的输入然后重新输入 `\mu`.

**Q3.** 为什么在有些环境中运行时不能得到正确结果, 如在 QQ 中输入 `\Mia` 时得到的结果不是 `𝑎`, 而是类似这样的 `𛽒`?

**A3.** 这是由于一些编辑器 (例如QQ输入框) 不支持所有的 `unicode` 字符导致的, 不是程序问题.

**Q4.** 程序为什么具有监听我键盘输入的权限?

**A4.** 这是 `pynput` 库支持的监听键盘输入, 其权限大致与一般输入法的相同, 程序不会储存或传输你输入的信息, 如果你对此感到担心可以查看源码.

**Q5.** 为什么有时可以打出文档中没有的字符?

**A5.** 符号表主要是借助 `Lean` 的符号得到的, 因此实际符号表包含若干额外的字符, 写代码时我认为没有必要删除, 如果你希望查看这些额外的字符或设定自己的字符, 请看 *高级设置* 一节并自行修改符号映射

**Q6.** 为什么不使用中文作为输入的语言?

**A6.** 这主要是考虑到 `TeX` 中有较为成熟的符号英文名, 可以直接借用 (且英文易于使用缩写). 且键盘监听到的时间是英文的字符, 而不是经过输入法输入的中文字符.
