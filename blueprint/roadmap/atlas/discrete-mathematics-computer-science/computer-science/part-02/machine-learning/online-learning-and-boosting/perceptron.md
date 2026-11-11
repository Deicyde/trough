---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Perceptron.sign, Cslib.MachineLearning.Perceptron.step, Cslib.MachineLearning.Perceptron.run, Cslib.MachineLearning.Perceptron.train, Cslib.MachineLearning.Perceptron.run_eq, Cslib.MachineLearning.Perceptron.classifies_of_run_eq_zero, Cslib.MachineLearning.Perceptron.run_invariant, Cslib.MachineLearning.Perceptron.mistakes_mul_sq_le
statement: formalized
proof: formalized
---

# Perceptron

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html).

## Sign of a Boolean label

For a commutative ring $K$, the sign of a Boolean label $y$ is
the element $\operatorname{sign}(y) \in K$ equal to $1$ if $y$ is true and to $-1$ if $y$ is
false.

Formalized by `Cslib.MachineLearning.Perceptron.sign`, a definition declared in [CSLibExt/MachineLearning/Perceptron.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#sign).

## Perceptron step

Let $K$ be a commutative ring with a linear order, $\iota$ a finite type,
and $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on $K^\iota$. One perceptron step
takes a state $(w, m)$, made of weights $w \in K^\iota$ and a mistake count $m \in \mathbb{N}$, and
a labelled example $(x, y)$ with $x \in K^\iota$ and $y$ a Boolean. If
$\operatorname{sign}(y)\,(w \cdot x) \le 0$, that is, $w$ does not classify the example strictly
correctly, the step returns $(w + \operatorname{sign}(y)\,x,\ m + 1)$ and counts a mistake;
otherwise it returns $(w, m)$ unchanged.

Formalized by `Cslib.MachineLearning.Perceptron.step`, a definition declared in [CSLibExt/MachineLearning/Perceptron.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#step).

## Perceptron run

Let $K$ be a commutative ring with a linear order and $\iota$ a finite type.
The run of the perceptron over a finite list $L$ of labelled examples $(x, y)$, with
$x \in K^\iota$ and $y$ a Boolean, from weights $w \in K^\iota$ with $m \in \mathbb{N}$ mistakes so
far is the pair of final weights and final mistake count obtained by applying the perceptron step
to each example of $L$ in order, starting from the state $(w, m)$.

Formalized by `Cslib.MachineLearning.Perceptron.run`, a definition declared in [CSLibExt/MachineLearning/Perceptron.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#run).

## Perceptron training

Given a finite list $D$ of labelled examples, a number $n$ of passes
and weights $w$, training returns nothing when $n = 0$. When $n = m + 1$, it runs one perceptron
pass over $D$ from $w$ with mistake count $0$; if that pass makes no mistake it returns $w$, and
otherwise it trains on $D$ for $m$ passes from the weights the pass produced. So training repeats
passes until one makes no mistake, for at most $n$ passes, and returns the weights of that pass,
or nothing if every pass made a mistake.

Formalized by `Cslib.MachineLearning.Perceptron.train`, a definition declared in [CSLibExt/MachineLearning/Perceptron.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#train).

## The starting mistake count only shifts the final count

Let $K$ be a commutative ring
with a linear order and $\iota$ a finite type, and let $L$ be a finite list of labelled examples
$(x, y)$ with $x \in K^\iota$ and $y$ a Boolean. For all weights $w \in K^\iota$ and every natural
number $m$, the perceptron run over $L$ from $w$ with $m$ mistakes so far ends with the same weights
as the run from $w$ with $0$ mistakes so far, and with mistake count $m + c$, where $c$ is the final
mistake count of the run from $w$ with $0$ mistakes so far.

Formalized by `Cslib.MachineLearning.Perceptron.run_eq`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#run-eq).

## A mistake-free pass classifies every example

Let $K$ be a commutative ring with a linear
order, $\iota$ a finite type, and $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on
$K^\iota$. Let $L$ be a finite list of labelled examples $(x, y)$ with $x \in K^\iota$ and $y$ a
Boolean, and let $w \in K^\iota$. If the perceptron run over $L$ from weights $w$ with $0$ mistakes
so far ends with mistake count $0$, then every example $(x, y)$ in $L$ satisfies
$0 < \operatorname{sign}(y)\,(w \cdot x)$.

Formalized by `Cslib.MachineLearning.Perceptron.classifies_of_run_eq_zero`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#classifies-of-run-eq-zero).

## Invariant of the perceptron run

Let $K$ be a linearly ordered commutative ring, $\iota$ a
finite type, $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on $K^\iota$, $u \in K^\iota$
and $\gamma, R \in K$. Let $L$ be a finite list of labelled examples $(x, y)$ with $x \in K^\iota$
and $y$ a Boolean, such that every example in $L$ satisfies
$\gamma \le \operatorname{sign}(y)\,(u \cdot x)$ and $x \cdot x \le R^2$. Let $w \in K^\iota$ and
$m \in \mathbb{N}$ satisfy $m \gamma \le u \cdot w$ and $w \cdot w \le m R^2$, and let the
perceptron run over $L$ from $w$ with $m$ mistakes so far end with weights $w'$ and mistake count
$m'$. Then $m' \gamma \le u \cdot w'$ and $w' \cdot w' \le m' R^2$.

Formalized by `Cslib.MachineLearning.Perceptron.run_invariant`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#run-invariant).

## Novikoff's perceptron mistake bound

Let $K$ be a linearly ordered commutative ring,
$\iota$ a finite type, $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on $K^\iota$,
$u \in K^\iota$, and $\gamma, R \in K$ with $\gamma > 0$. Let $L$ be a finite list of labelled
examples $(x, y)$ with $x \in K^\iota$ and $y$ a Boolean, such that every example in $L$ satisfies
$\gamma \le \operatorname{sign}(y)\,(u \cdot x)$ and $x \cdot x \le R^2$. If the perceptron run
over $L$ from the zero weights with $0$ mistakes so far ends with mistake count $k$, then
$k \gamma^2 \le (u \cdot u) R^2$.

Formalized by `Cslib.MachineLearning.Perceptron.mistakes_mul_sq_le`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#mistakes-mul-sq-le).

## Novikoff's mistake bound over an ordered field

Let $F$ be a linearly ordered field,
$\iota$ a finite type, $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on $F^\iota$,
$u \in F^\iota$, and $\gamma, R \in F$ with $\gamma > 0$. Let $L$ be a finite list of labelled
examples $(x, y)$ with $x \in F^\iota$ and $y$ a Boolean, such that every example in $L$ satisfies
$\gamma \le \operatorname{sign}(y)\,(u \cdot x)$ and $x \cdot x \le R^2$. If the perceptron run
over $L$ from the zero weights with $0$ mistakes so far ends with mistake count $k$, then
$k \le (u \cdot u) R^2 / \gamma^2$; for a unit vector $u$ this is the textbook bound
$R^2 / \gamma^2$.

Formalized by `Cslib.MachineLearning.Perceptron.mistakes_le_div`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#mistakes-le-div).

## Trained weights classify every example

Let $K$ be a commutative ring with a linear order,
$\iota$ a finite type, and $v \cdot w = \sum_{i \in \iota} v_i w_i$ the dot product on $K^\iota$.
Let $L$ be a finite list of labelled examples $(x, y)$ with $x \in K^\iota$ and $y$ a Boolean. For
every natural number $n$ and all weights $w, v \in K^\iota$, if training on $L$ from $w$ with at
most $n$ passes returns $v$, then every example $(x, y)$ in $L$ satisfies
$0 < \operatorname{sign}(y)\,(v \cdot x)$.

Formalized by `Cslib.MachineLearning.Perceptron.train_classifies`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#train-classifies).

## Every failed training pass adds a mistake

Let $K$ be a commutative ring with a linear
order and $\iota$ a finite type, and let $L$ be a finite list of labelled examples $(x, y)$ with
$x \in K^\iota$ and $y$ a Boolean. For every natural number $n$ and all weights $w \in K^\iota$, if
training on $L$ from $w$ with at most $n$ passes returns no weights, then the perceptron run from
$w$ with $0$ mistakes so far over the concatenation of $n$ copies of $L$ ends with a mistake count
of at least $n$.

Formalized by `Cslib.MachineLearning.Perceptron.le_run_of_train_eq_none`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#le-run-of-train-eq-none).

## The perceptron converges

Let $K$ be a linearly ordered commutative ring, let $\iota$ be a
finite index type, write $a \cdot b = \sum_{j \in \iota} a_j b_j$ for $a, b \in K^\iota$, and let
the label sign $s(y)$ be $1$ if the Boolean $y$ is true and $-1$ otherwise. Let $D$ be a finite
list of examples $(x, y)$ with $x \in K^\iota$ and $y$ a Boolean, and let $u \in K^\iota$ and
$\gamma, R \in K$ with $\gamma > 0$ be such that every example $(x, y)$ of $D$ satisfies
$\gamma \le s(y)\,(u \cdot x)$ and $x \cdot x \le R^2$. Then for every natural number $n$ with
$(u \cdot u) R^2 < n \gamma^2$, perceptron training on $D$ from the zero weights with at most $n$
passes returns some weights $v$, and $0 < s(y)\,(v \cdot x)$ for every example $(x, y)$ of $D$.

Formalized by `Cslib.MachineLearning.Perceptron.train_converges`, a theorem declared in [CSLibExt/MachineLearning/Perceptron.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Perceptron.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html#train-converges).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perceptron](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/online-learning-and-boosting/perceptron)
