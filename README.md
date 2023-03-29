# 数学表达式转LaTeX文档教程

- update 03-29 version 1.15

本教程将向您详细介绍如何使用Python脚本[`math_to_latex.py`](https://github.com/MaomaoYsr/MATH-to-LateX/blob/main/math_to_latex.py)来将数学表达式转换为LaTeX代码并生成Markdown文档。


### 更新日志

#### 版本 1.1 - 2023-03-27
1. **注释支持**：现在您可以在输入文件 `expressions.txt` 中的数学表达式后添加注释。注释需要在表达式后紧跟一个 `#` 符号，然后在该符号后写下您的注释内容。

2. **扩展数学类型支持**：脚本现在支持偏导数、导数和积分。您可以使用 `partial`、`prime` 和 `integrate` 作为前缀。

3. **兼容性优化**：脚本现在将 '^' 替换为 '**'，以便与 Sympy 库兼容。

4. **错误提示**：脚本现在会在遇到错误时打印详细的错误信息，以便于用户识别问题所在。

5. **Bug 修复** 对程序进行改进，修复了部分表达式无法运行程序的bug


## 环境准备
1.安装Python 3：请确保您的计算机上安装了Python 3。您可以在这里下载和安装Python 3：https://www.python.org/downloads/

2.安装所需的Python库：在命令行中运行以下命令来安装`sympy`和`markdown`库（pycharm：在python package查找安装）

```
pip install sympy
pip install markdown
```
3.下载脚本：将我们为您编写的[`math_to_latex.py`](https://github.com/MaomaoYsr/MATH-to-LateX/blob/main/math_to_latex.py)脚本保存到本地文件夹。

## 使用方法
1.准备输入文件：创建一个名为`expressions.txt`的文本文件，将您要转换的数学表达式逐行输入。每个表达式单独占据一行。

现在您可以在表达式后面添加注释。注释需要在表达式后紧跟一个`#`符号，然后在该符号后写下您的注释内容。


例如：
```
f(x)=2*ln(x) # 对数函数
g(x)=x^2 - 5x + 6 # 二次函数
h(x)=sqrt(x) # 平方根函数
```
2.运行脚本：双击`math_to_latex.py`脚本或在命令行中运行`python math_to_latex.py`。

脚本将自动读取`expressions.txt`文件中的数学表达式，
将它们转换为LaTeX代码，并将结果保存在名为`output.md`的Markdown文档中。

3.查看输出：打开生成的`output.md`文件，您将看到转换后的LaTeX代码，例如：
```
$$
f{\left(x \right)} = 2 \ln{\left(x \right)}
$$

$$
g{\left(x \right)} = x^{2} - 5 x + 6
$$

$$
h{\left(x \right)} = \sqrt{x}
$$
（在GitHub中可查看转换后的效果）
```


4.使用Markdown编辑器：将`output.md`文件导入支持LaTeX数学公式的Markdown编辑器或网站（如Jupyter Notebook、Typora等），以查看和编辑这些数学公式。

## 支持的数学类型
- 方程：如 x^2 + 2x + 1 = 0。
- 函数定义：如 f(x) = 2 * ln(x)。
- 算术表达式：如 2 * (x - 3) / (x + 1)。
- 常见数学运算符：加（+）、减（-）、乘（*）、除（/）、指数（^或**）等。
- 常见数学函数：如sin(x)、cos(x)、tan(x)、ln(x)、log(x)（以10为底的对数）、sqrt(x)（平方根）等。
- 偏导数、导数和积分：脚本现在支持偏导数、导数和积分。您可以使用 `partial`、`prime` 和 `integrate` 作为前缀。
   - 例如：
          
          
            y = x^2 + 2x # 定义一个函数
            y_prime = prime(y) # 计算导数
            y_partial_x = partial(y, x) # 计算偏导数
            integral_y = integrate(y, x) # 计算积分

          
## 注意事项

1. 在渲染Markdown的应用程序或网站上，您可能需要启用MathJax以正确显示LaTeX数学公式。

2. 本脚本支持方程、函数定义、算术表达式等。如果在转换过程中遇到任何问题，请确保您的输入表达式遵循常见的数学表示法。

3. 如果您需要更改输入文件名或输出文件名，可以直接在脚本的`main()`函数调用中更改参数，如下所示：

   ```
   if __name__ == "__main__":
       main(input_file='your_input_file.txt', output_file='your_output_file.md')
   ```

4.如果您发现某些特定的数学符号或函数没有正确转换，请检查输入表达式以确保它们遵循常见的数学表示法。此外，您可以手动修改生成的LaTeX代码以解决问题。


5.请注意，脚本对输入表达式的语法和格式有一定的容错能力。为了确保正确的转换结果，请尽量确保输入表达式的准确性。


6.该脚本并未涵盖所有可能的数学符号和表达式。对于一些特殊的数学符号或较复杂的表达式，您可能需要手动编辑生成的LaTeX代码以获得正确的显示效果。


7.在未来的更新中会添加更多功能
