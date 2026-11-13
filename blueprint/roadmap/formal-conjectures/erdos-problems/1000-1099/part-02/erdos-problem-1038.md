---
declaration: theorem
origin: cited
lean: Erdos1038.erdos_1038.parts.i, Erdos1038.erdos_1038.parts.ii, Erdos1038.erdos_1038.variants.inf_upperBound, Erdos1038.erdos_1038.variants.inf_lowerBound, Erdos1038.erdos_1038.variants.quadratic_sublevel_formula, Erdos1038.erdos_1038.variants.quadratic_upperBound, Erdos1038.erdos_1038.variants.quadratic_extremizer, Erdos1038.erdos_1038.variants.sup_lowerBound, Erdos1038.erdos_1038.variants.inf_lt_two
statement: formalized
---

# Erdős Problem 1038

> *Reference:*
>  - [erdosproblems.com/1038](https://www.erdosproblems.com/1038)
>  - [Tao25] Tao, Terence. Sublevel Sets of Logarithmic Potentials. Terry Tao’s Blog, Dec. 2025
>   (https://terrytao.wordpress.com/wp-content/uploads/2025/12/erdos-1038-1.pdf)
>  - [EHP58] Erdős, P., Herzog, F., Piranian, G. Metric properties of polynomials.
>   J. Analyse Math. 6 (1958), 125--148.

*Quoted from [FormalConjectures/ErdosProblems/1038.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1038](https://www.erdosproblems.com/1038).

The file states 9 research or textbook statements: 1 open, 3 solved and 5 textbook results.

## `Erdos1038.erdos_1038.parts.i`

Open: stated without proof.

> What is the infimum of `|{x ∈ ℝ : |f x| < 1}|` over all nonconstant monic polynomials `f` such
> that all of its roots are real and contained in `[-1,1]`?

```lean
theorem erdos_1038.parts.i : erdos_1038.parts.i.answer =
    ⨅ f : {f : Polynomial ℝ // f.Monic ∧ f ≠ 1 ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1}
```

Category `research open`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L44).

## `Erdos1038.erdos_1038.parts.ii`

Solved: stated here without proof.

> The supremum of `|{x ∈ ℝ : |f x| < 1}|` over all monic polynomials `f` such that
> all of its roots are real and contained in `[-1,1]` is `2 * 2 ^ (1 / 2)`. This is proved in
> [Tao25].

```lean
theorem erdos_1038.parts.ii : 2 * 2 ^ (1 / 2 : ℝ) =
    ⨆ f : {f : Polynomial ℝ // f.Monic ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1}
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L54).

## `Erdos1038.erdos_1038.variants.inf_upperBound`

Solved: stated here without proof.

> The infimum of `|{x ∈ ℝ : |f x| < 1}|` over all nonconstant monic polynomials `f` such that
> all of its roots are real and contained in `[-1,1]` is `< 1.835`.

```lean
theorem erdos_1038.variants.inf_upperBound : ⨅ f : {f : Polynomial ℝ // f.Monic ∧ f ≠ 1 ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1} < 1.835
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L63).

## `Erdos1038.erdos_1038.variants.inf_lowerBound`

Solved: stated here without proof.

> The infimum of `|{x ∈ ℝ : |f x| < 1}|` over all nonconstant monic polynomials `f` such that
> all of its roots are real and contained in `[-1,1]` is `≥ 2 ^ (4 / 3) - 1`.

```lean
theorem erdos_1038.variants.inf_lowerBound : 2 ^ (4 / 3 : ℝ) - 1 ≤
    ⨅ f : {f : Polynomial ℝ // f.Monic ∧ f ≠ 1 ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1}
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L71).

## `Erdos1038.erdos_1038.variants.quadratic_sublevel_formula`

Textbook result, proved here.

> For a monic quadratic with roots at distance at most two, the sublevel measure
> is $2\sqrt{1+d^2}$, where $2|d|$ is the distance between the roots. This gives
> the degree-two case of the sublevel-set problem in [Tao25].

```lean
theorem erdos_1038.variants.quadratic_sublevel_formula (m d : ℝ) (hd : |d| ≤ 1) :
    volume {x : ℝ | |(x - m) ^ 2 - d ^ 2| < 1} =
      ENNReal.ofReal (2 * Real.sqrt (1 + d ^ 2))
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L82).

## `Erdos1038.erdos_1038.variants.quadratic_upperBound`

Textbook result, proved here.

> The degree-two case of the supremum bound in [Tao25]: if $a,b\in[-1,1]$,
> the sublevel set of $(x-a)(x-b)$ has measure at most $2\sqrt{2}$.

```lean
theorem erdos_1038.variants.quadratic_upperBound (a b : ℝ) (ha : |a| ≤ 1) (hb : |b| ≤ 1) :
    volume {x : ℝ | |(x-a)*(x-b)| < 1} ≤ ENNReal.ofReal (2 * Real.sqrt 2)
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L118).

## `Erdos1038.erdos_1038.variants.quadratic_extremizer`

Textbook result, proved here.

> The admissible quadratic $x^2-1$, with roots $-1$ and $1$, attains the supremum
> value $2\sqrt{2}$ in [Tao25].

```lean
theorem erdos_1038.variants.quadratic_extremizer :
    volume {x : ℝ | |x ^ 2 - 1| < 1} = ENNReal.ofReal (2 * Real.sqrt 2)
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L136).

## `Erdos1038.erdos_1038.variants.sup_lowerBound`

Textbook result, proved here.

> The lower half of `erdos_1038.parts.ii`: the supremum is at least $2\sqrt{2}$, because the
> admissible polynomial $x^2-1$ has sublevel measure exactly $2\sqrt{2}$. The matching upper bound
> is proved in [Tao25].

```lean
theorem erdos_1038.variants.sup_lowerBound : 2 * 2 ^ (1 / 2 : ℝ) ≤
    ⨆ f : {f : Polynomial ℝ // f.Monic ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1}
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L146).

## `Erdos1038.erdos_1038.variants.inf_lt_two`

Textbook result, proved here.

> The infimum in `erdos_1038.parts.i` is strictly less than $2$, as observed in [EHP58]:
> for $f(x)=(x+1)(x-1)^3$ the sublevel set $\{x : |f(x)| < 1\}$ is contained in
> $(-1.108,-0.835)\cup(0,1.718)$, whose total length is $1.991$.

```lean
theorem erdos_1038.variants.inf_lt_two : ⨅ f : {f : Polynomial ℝ // f.Monic ∧ f ≠ 1 ∧
    (f.roots.filter fun x => x ∈ Set.Icc (-1 : ℝ) 1).card = f.natDegree},
    volume {x | |f.1.eval x| < 1} < 2
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1038.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean#L164).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1038.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1038.lean)
- [erdosproblems.com/1038](https://www.erdosproblems.com/1038)
