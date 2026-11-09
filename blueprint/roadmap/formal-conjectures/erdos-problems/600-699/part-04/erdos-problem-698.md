---
declaration: theorem
origin: cited
lean: Erdos698.erdos_698, Erdos698.erdos_698.variants.erdos_szekeres, Erdos698.erdos_698.variants.erdos_szekeres_sharp, Erdos698.erdos_698.variants.bergman
statement: formalized
---

# Erdős Problem 698

> *References:*
> - [erdosproblems.com/698](https://www.erdosproblems.com/698)
> - [ErSz78] Erdős, P. and Szekeres, G., *Some number theoretic problems on binomial
>   coefficients*. Austral. Math. Soc. Gaz. (1978), 97-99.
> - [Be11] Bergman, George M., *On common divisors of multinomial coefficients*. Bull. Aust.
>   Math. Soc. (2011), 138--157.

*Quoted from [FormalConjectures/ErdosProblems/698.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/698](https://www.erdosproblems.com/698).

The file states 4 research or textbook statements: 4 solved.

## `Erdos698.erdos_698`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos698.lean#L452](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos698.lean#L452).

> Is there some $h(n)\to \infty$ such that for all $2\leq i\lt j\leq n/2$
>
> $$\textrm{gcd}\left( \binom{n}{i},\binom{n}{j}\right) \geq h(n)?$$
>
> This was resolved by Bergman [Be11], who proved that for any $2\leq i\lt j\leq n/2$
>
> $$\textrm{gcd}\left( \binom{n}{i},\binom{n}{j}\right) \gg n^{1/2}\frac{2^i}{i^{3/2}},$$
>
> where the implied constant is absolute.
>
> The linked formal proof (van Doorn and Aristotle, see `erdos_698.variants.bergman`) gives the
> explicit bound $\gcd > \frac{2^i \sqrt n}{4 i \sqrt{i - 1}}$, so $h(n) = \lfloor \sqrt n / 4 \rfloor$
> works since $i \sqrt{i - 1} \le 2^i$ for $i \ge 2$.

```lean
theorem erdos_698 :
    ∃ h : ℕ → ℕ, Tendsto h atTop atTop ∧
      ∀ n i j : ℕ, 2 ≤ i → i < j → j ≤ n / 2 →
        h n ≤ Nat.gcd (n.choose i) (n.choose j)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/698.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean#L52).

## `Erdos698.erdos_698.variants.erdos_szekeres`

Proved here.

> A problem of Erdős and Szekeres, who observed that
>
> $$\textrm{gcd}\left( \binom{n}{i},\binom{n}{j}\right) \geq \frac{\binom{n}{i}}{\binom{j}{i}}
> \geq 2^i$$
>
> (in particular the greatest common divisor is always $>1$).

```lean
theorem erdos_698.variants.erdos_szekeres (n i j : ℕ) (hi : 1 ≤ i) (hij : i < j)
    (hj : j ≤ n / 2) :
    (n.choose i : ℝ) / (j.choose i : ℝ) ≤ (Nat.gcd (n.choose i) (n.choose j) : ℝ) ∧
      (2 : ℝ) ^ i ≤ (n.choose i : ℝ) / (j.choose i : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/698.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean#L65).

## `Erdos698.erdos_698.variants.erdos_szekeres_sharp`

Proved here.

> This inequality is sharp for $i=1$, $j=p$, and $n=2p$.

```lean
theorem erdos_698.variants.erdos_szekeres_sharp (p : ℕ) (hp : p.Prime) (hp2 : 2 < p) :
    (Nat.gcd ((2 * p).choose 1) ((2 * p).choose p) : ℝ) =
        ((2 * p).choose 1 : ℝ) / (p.choose 1 : ℝ) ∧
      ((2 * p).choose 1 : ℝ) / (p.choose 1 : ℝ) = (2 : ℝ) ^ 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/698.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean#L114).

## `Erdos698.erdos_698.variants.bergman`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos698.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos698.lean).

> This was resolved by Bergman [Be11], who proved that for any $2\leq i\lt j\leq n/2$
>
> $$\textrm{gcd}\left( \binom{n}{i},\binom{n}{j}\right) \gg n^{1/2}\frac{2^i}{i^{3/2}},$$
>
> where the implied constant is absolute.

```lean
theorem erdos_698.variants.bergman :
    ∃ c : ℝ, 0 < c ∧ ∀ n i j : ℕ, 2 ≤ i → i < j → j ≤ n / 2 →
      c * (Real.sqrt (n : ℝ) * (2 : ℝ) ^ i / ((i : ℝ) * Real.sqrt (i : ℝ))) ≤
        (Nat.gcd (n.choose i) (n.choose j) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/698.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean#L164).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/698.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/698.lean)
- [erdosproblems.com/698](https://www.erdosproblems.com/698)
