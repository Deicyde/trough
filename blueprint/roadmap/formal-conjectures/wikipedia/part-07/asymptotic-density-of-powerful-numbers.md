---
declaration: theorem
origin: cited
lean: PowerfulNumbersDensity.asymptotic_erdos_szekeres, PowerfulNumbersDensity.asymptotic_bateman_grosswald, PowerfulNumbersDensity.error_term_improvement
statement: formalized
---

# Asymptotic density of powerful numbers

> Let $Q(x)$ denote the number of powerful integers up to $x$. Erdős and Szekeres [ES35] proved
> $$Q(x) = \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + O(x^{1/3}),$$
> and Bateman and Grosswald [BG58] sharpened this to
> $$Q(x) = \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + \frac{\zeta(2/3)}{\zeta(2)} x^{1/3} + O(x^{1/6}).$$
> Improving the exponent $1/6$ in the error term unconditionally remains open; conditional
> improvements are known under the Riemann Hypothesis.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Powerful_number)
> - [ES35] Erdős, P. and Szekeres, G., *Über die Anzahl der Abelschen Gruppen gegebener Ordnung
>   und über ein verwandtes zahlentheoretisches Problem*, Acta Sci. Math. (Szeged) 7 (1935), 95–102.
> - [BG58] Bateman, P. T. and Grosswald, E., *On a theorem of Erdős and Szekeres*,
>   Illinois J. Math. 2 (1958), 88–98.

*Quoted from [FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `PowerfulNumbersDensity.asymptotic_erdos_szekeres`

Solved: stated here without proof.

> Erdős and Szekeres [ES35] proved that the number of powerful integers up to $x$ satisfies
> $$Q(x) = \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + O(x^{1/3}).$$
> In particular $Q(x) \sim \frac{\zeta(3/2)}{\zeta(3)} \sqrt{x}$.

```lean
theorem asymptotic_erdos_szekeres :
    (fun x : ℝ => (Q x : ℝ) - A * x ^ ((1 : ℝ) / 2)) =O[atTop]
      fun x => x ^ ((1 : ℝ) / 3)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean#L60).

## `PowerfulNumbersDensity.asymptotic_bateman_grosswald`

Solved: stated here without proof.

> Bateman and Grosswald [BG58] proved the sharper asymptotic
> $$Q(x) = \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + \frac{\zeta(2/3)}{\zeta(2)} x^{1/3} + O(x^{1/6}).$$

```lean
theorem asymptotic_bateman_grosswald :
    (fun x : ℝ => (Q x : ℝ) - A * x ^ ((1 : ℝ) / 2) - B * x ^ ((1 : ℝ) / 3)) =O[atTop]
      fun x => x ^ ((1 : ℝ) / 6)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean#L70).

## `PowerfulNumbersDensity.error_term_improvement`

Open: stated without proof.

> Can the exponent $1/6$ in the error term of the Bateman–Grosswald asymptotic be improved
> unconditionally? That is, is there $\delta > 0$ such that
> $$Q(x) = \frac{\zeta(3/2)}{\zeta(3)} x^{1/2} + \frac{\zeta(2/3)}{\zeta(2)} x^{1/3} +
> O(x^{1/6 - \delta})?$$
> Improvements are known under the Riemann Hypothesis.

```lean
theorem error_term_improvement :
    ∃ δ > (0 : ℝ),
      (fun x : ℝ => (Q x : ℝ) - A * x ^ ((1 : ℝ) / 2) - B * x ^ ((1 : ℝ) / 3)) =O[atTop]
        fun x => x ^ ((1 : ℝ) / 6 - δ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PowerfulNumbersDensity.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Powerful_number)
