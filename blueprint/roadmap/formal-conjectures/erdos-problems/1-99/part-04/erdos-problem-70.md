---
declaration: theorem
origin: cited
lean: Erdos70.erdos_70, Erdos70.erdos_70.variants.erdos_rado, Erdos70.erdos_70.variants.omega_times_two_four, Erdos70.erdos_70.variants.omega_three, Erdos70.erdos_70.variants.omega_one
statement: formalized
---

# Erdős Problem 70

> *References:*
> - [erdosproblems.com/70](https://www.erdosproblems.com/70)
> - [ErRa56] Erdős, P. and Rado, R., *A partition calculus in set theory*,
>   Bull. Amer. Math. Soc. **62** (1956), 427–489, Theorem 31.
> - [Er87] Erdős, P., *Some problems on finite and infinite graphs*,
>   Logic and combinatorics (Arcata, Calif., 1985), Contemp. Math. **65** (1987), 223–228.
>
> The 3-uniform (triple) partition relation $\mathfrak{c} \to (\beta, n)^3_2$, where
> $\mathfrak{c}$ denotes the order type of the real numbers with their usual order (written
> $\lambda$ in [ErRa56]). This is the triple analogue of `OrdinalCardinalRamsey` used in
> Problems 590–592; the file also contains the analogous relation for an ordinal in place
> of the real line.

*Quoted from [FormalConjectures/ErdosProblems/70.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/70](https://www.erdosproblems.com/70).

The file states 5 research or textbook statements: 3 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos70.erdos_70`

Open: stated without proof.

> **Erdős Problem 70**: Let $\mathfrak{c}$ be the order type of the real numbers,
> let $\beta$ be a countable ordinal, and let $2 \le n < \omega$.
> Is it true that $\mathfrak{c} \to (\beta, n)^3_2$?
>
> Note: The cases $n \le 3$ are trivially true (compare `omega_three`), so the
> genuine content of the conjecture begins at $n = 4$.

```lean
theorem erdos_70 :
    ∀ᵉ (β : Ordinal.{0}) (n : ℕ) (_ : β.card ≤ ℵ₀) (_ : 2 ≤ n),
      RealCardinalRamsey3 β n
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/70.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean#L113).

## `Erdos70.erdos_70.variants.erdos_rado`

Solved: stated here without proof.

> **Erdős–Rado partial result**: $\mathfrak{c} \to (\omega + n, 4)^3_2$ for any
> $2 \le n < \omega$, where $\mathfrak{c}$ is the order type of the real numbers.
> Positive partial answer to Problem 70 with $\beta = \omega + n$ and the blue side
> fixed at $4$ [ErRa56, Theorem 31].

```lean
theorem erdos_rado (n : ℕ) (hn : 2 ≤ n) :
    RealCardinalRamsey3 (ω + n) 4
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/70.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean#L129).

## `Erdos70.erdos_70.variants.omega_times_two_four`

Open: stated without proof.

> **First open case beyond Erdős–Rado**: $\mathfrak{c} \to (\omega \cdot 2, 4)^3_2$,
> where $\mathfrak{c}$ is the order type of the real numbers.
>
> Erdős and Rado proved $\mathfrak{c} \to (\omega + n, 4)^3_2$ for every finite $n \ge 2$
> (see `erdos_rado`), which covers all red ordinals below $\omega \cdot 2 = \omega + \omega$.
> This variant asks whether the result extends to $\beta = \omega \cdot 2$, the simplest
> countable ordinal not covered by their theorem.

```lean
theorem omega_times_two_four :
    RealCardinalRamsey3 (ω * 2) 4
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/70.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean#L143).

## `Erdos70.erdos_70.variants.omega_three`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/c024db0fa3ac32c6dddcd6c28d7b0cd994dad580/FormalConjectures/ErdosProblems/70.lean#L126](https://github.com/mo271/formal-conjectures/blob/c024db0fa3ac32c6dddcd6c28d7b0cd994dad580/FormalConjectures/ErdosProblems/70.lean#L126).

> **Trivial boundary case**: $\mathfrak{c} \to (\omega, 3)^3_2$, stated for the initial
> ordinal $\mathfrak{c}.\mathrm{ord}$ of the cardinality of the continuum.
>
> This is trivially true because in a 3-uniform hypergraph, a \"blue clique of size 3\"
> consists of a single 3-element subset ($\binom{3}{3} = 1$), so the blue alternative
> merely asks for one blue triple to exist. The proof splits into two cases:
> - If any blue triple exists, it is itself a blue-monochromatic set of cardinality 3.
> - If no blue triple exists, all triples are red, and since $\omega \le \mathfrak{c}$,
>   any subset of order type $\omega$ is red-monochromatic.
>
> The problem becomes non-trivial only for $n \ge 4$; see `omega_times_two_four` for
> the simplest genuinely open case.

```lean
theorem omega_three :
    OrdinalCardinalRamsey3 (𝔠).ord ω 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/70.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean#L164).

## `Erdos70.erdos_70.variants.omega_one`

Open: stated without proof.

> **The relation at $\omega_1$**: $\mathfrak{c} \to (\omega_1, n)^3_2$ for finite $n \ge 2$,
> where $\omega_1 = \aleph_1$ is the first uncountable ordinal.
>
> Note that $\omega_1$ is *not* a countable ordinal, so this is not directly an instance of the
> main Erdős problem (which asks for *countable* $\beta$). Under CH, $\omega_1 = \mathfrak{c}.\mathrm{ord}$,
> making this a self-referential question about $\mathfrak{c}.\mathrm{ord} \to
> (\mathfrak{c}.\mathrm{ord}, n)^3_2$.

```lean
theorem omega_one :
    ∀ᵉ (n : ℕ) (_ : 2 ≤ n),
      OrdinalCardinalRamsey3 (𝔠).ord (Cardinal.aleph 1).ord n
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/70.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean#L178).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/70.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/70.lean)
- [erdosproblems.com/70](https://www.erdosproblems.com/70)
