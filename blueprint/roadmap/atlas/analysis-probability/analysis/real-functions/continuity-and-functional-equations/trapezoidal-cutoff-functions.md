---
declaration: section
origin: cited
lean: Real.intervalCutoff, Real.intervalCutoff_nonneg, Real.intervalCutoff_le_one, Real.intervalCutoff_continuous, Real.intervalCutoff_eq_zero_left, Real.intervalCutoff_eq_zero_right, Real.intervalCutoff_zero_width, Real.intervalCutoff_eq_zero_of_le
statement: formalized
proof: formalized
---

# Trapezoidal cutoff functions

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html).

## Interval cutoff

For real numbers $a$, $b$ and $\delta$, the interval cutoff is the
function $\chi_{a,b,\delta} \colon \mathbb{R} \to \mathbb{R}$ defined by

$$
\chi_{a,b,\delta}(x) = \max\{0, \min\{1, (x - a)/\delta, (b - x)/\delta\}\},
$$

where division by zero is taken to give $0$.

It vanishes at $a$ and at $b$. For $\delta > 0$ it equals $1$ on $[a + \delta, b - \delta]$, which
is nonempty when $2\delta \le b - a$; for $\delta = 0$ it is identically zero.

Formalized by `Real.intervalCutoff`, a definition declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff).

## The interval cutoff is nonnegative

For all real numbers $a$, $b$, $\delta$ and $x$, the
interval cutoff $\chi_{a,b,\delta}$ with endpoints $a$, $b$ and width $\delta$ satisfies
$0 \le \chi_{a,b,\delta}(x)$.

Formalized by `Real.intervalCutoff_nonneg`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-nonneg).

## The interval cutoff is at most one

For all real numbers $a$, $b$, $\delta$ and $x$, the
interval cutoff $\chi_{a,b,\delta}$ with endpoints $a$, $b$ and width $\delta$ satisfies
$\chi_{a,b,\delta}(x) \le 1$.

Formalized by `Real.intervalCutoff_le_one`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-le-one).

## Continuity of the interval cutoff

For all real numbers $a$, $b$ and $\delta$, including
$\delta = 0$, the interval cutoff $\chi_{a,b,\delta} \colon \mathbb{R} \to \mathbb{R}$ with
endpoints $a$, $b$ and width $\delta$ is continuous.

Formalized by `Real.intervalCutoff_continuous`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-continuous).

## The interval cutoff vanishes at the left endpoint

For all real numbers $a$, $b$ and
$\delta$, the interval cutoff $\chi_{a,b,\delta}$ with endpoints $a$, $b$ and width $\delta$
satisfies $\chi_{a,b,\delta}(a) = 0$.

Formalized by `Real.intervalCutoff_eq_zero_left`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-eq-zero-left).

## The interval cutoff vanishes at the right endpoint

For all real numbers $a$, $b$ and
$\delta$, the interval cutoff $\chi_{a,b,\delta}$ with endpoints $a$, $b$ and width $\delta$
satisfies $\chi_{a,b,\delta}(b) = 0$.

Formalized by `Real.intervalCutoff_eq_zero_right`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-eq-zero-right).

## The interval cutoff of zero width vanishes

For all real numbers $a$, $b$ and $x$, the
interval cutoff $\chi_{a,b,0}$ with endpoints $a$, $b$ and width $0$ satisfies
$\chi_{a,b,0}(x) = 0$.

Formalized by `Real.intervalCutoff_zero_width`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-zero-width).

## The interval cutoff vanishes left of the interval

For real numbers $a$, $b$, $\delta$
and $x$ with $\delta > 0$ and $x \le a$, the interval cutoff $\chi_{a,b,\delta}$ with endpoints
$a$, $b$ and width $\delta$ satisfies $\chi_{a,b,\delta}(x) = 0$.

Formalized by `Real.intervalCutoff_eq_zero_of_le`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-eq-zero-of-le).

## The interval cutoff vanishes right of the interval

For real numbers $a$, $b$, $\delta$
and $x$ with $\delta > 0$ and $b \le x$, the interval cutoff $\chi_{a,b,\delta}$ with endpoints
$a$, $b$ and width $\delta$ satisfies $\chi_{a,b,\delta}(x) = 0$.

Formalized by `Real.intervalCutoff_eq_zero_of_ge`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-eq-zero-of-ge).

## The interval cutoff equals one on its plateau

For real numbers $a$, $b$, $\delta$ and $x$
with $\delta > 0$ and $a + \delta \le x \le b - \delta$, the interval cutoff $\chi_{a,b,\delta}$
with endpoints $a$, $b$ and width $\delta$ satisfies $\chi_{a,b,\delta}(x) = 1$.

Formalized by `Real.intervalCutoff_eq_one`, a theorem declared in [MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ContinuousFunction/IntervalCutoff.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html#interval-cutoff-eq-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trapezoidal cutoff functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/trapezoidal-cutoff-functions)
