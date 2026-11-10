---
declaration: theorem
origin: cited
lean: Erdos118.erdos_118, Erdos118.erdos_118.variants.larson
statement: formalized
---

# Erdős Problem 118

> *Reference:* [erdosproblems.com/118](https://www.erdosproblems.com/118)
>
> *References:*
> - [Sc99] Schipperus, R. *Countable partition ordinals.* Thesis, University of Colorado (1999).
> - [Sc10] Schipperus, R. *Countable partition ordinals.* Ann. Pure Appl. Logic 161 (2010),
>   1195–1215.
> - [Da99] Darby, C. *Negative partition relations for ordinals $\omega^{\omega^\delta}$.*
>   J. Combin. Theory Ser. B 76 (1999), 205–222.
> - [La00] Larson, J. A. *An ordinal partition avoiding pentagrams.* J. Symbolic Logic 65
>   (2000), 969–978.
> - [HST10] Hajnal, A.; Larson, J. A. *Partition relations.* Handbook of set theory,
>   Springer (2010), 129–213.

*Quoted from [FormalConjectures/ErdosProblems/118.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/118.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/118](https://www.erdosproblems.com/118).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos118.erdos_118`

Solved: stated here without proof.

> **Erdős Problem 118** (problem of Erdős and Hajnal). Let $\alpha$ be such that
> $\alpha \to (\alpha, 3)^2$. For every $n \ge 3$, must $\alpha \to (\alpha, n)^2$?
>
> The original question is asked for cardinals, ordinals, and order types; we state the
> ordinal version, which is the standard reading: ordinals $\alpha$ with
> $\alpha \to (\alpha, 3)^2$ are called *partition ordinals*.
>
> The answer is **no**, shown independently by Schipperus [Sc99, Sc10] and Darby [Da99].
> Larson [La00] gave the concrete counterexample $\alpha = \omega^{\omega^2}$, for which
> $\alpha \to (\alpha, 3)^2$ holds yet $\alpha \not\to (\alpha, 5)^2$. See Chapter 2.9 of
> [HST10] for further background.

```lean
theorem erdos_118 :
    ¬ ∀ α : Ordinal.{0}, OrdinalRamsey α α 3 →
      ∀ n : ℕ, 3 ≤ n → OrdinalRamsey α α n
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/118.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/118.lean#L74).

## `Erdos118.erdos_118.variants.larson`

Solved: stated here without proof.

> **Larson (2000).** The ordinal $\alpha = \omega^{\omega^2}$ is a partition ordinal,
> $\omega^{\omega^2} \to (\omega^{\omega^2}, 3)^2$, yet
> $\omega^{\omega^2} \not\to (\omega^{\omega^2}, 5)^2$ [La00], so the answer to the
> Erdős–Hajnal question is negative already at $n = 5$.

```lean
theorem larson : OrdinalRamsey (ω ^ ω ^ (2 : Ordinal)) (ω ^ ω ^ (2 : Ordinal)) 3 ∧
    ¬ OrdinalRamsey (ω ^ ω ^ (2 : Ordinal)) (ω ^ ω ^ (2 : Ordinal)) 5
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/118.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/118.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/118.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/118.lean)
- [erdosproblems.com/118](https://www.erdosproblems.com/118)
