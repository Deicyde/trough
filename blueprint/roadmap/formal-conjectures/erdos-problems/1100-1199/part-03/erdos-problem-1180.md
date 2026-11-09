---
declaration: theorem
origin: cited
lean: Erdos1180.erdos_1180, Erdos1180.erdos_1180.variants.shparlinski, Erdos1180.erdos_1180.variants.glibichuk, Erdos1180.erdos_1180.variants.lower_bound, Erdos1180.erdos_1180.variants.optimal
statement: formalized
---

# Erdős Problem 1180

> *References:*
> - [erdosproblems.com/1180](https://www.erdosproblems.com/1180)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Sh02] Shparlinski, Igor E., *On a question of Erdős and Graham*. Arch. Math. (Basel) (2002),
>   445-448.
> - [Gl06] Glibichuk, A. A., *Combinatorial properties of sets of residues modulo a prime and the
>   Erdős-Graham problem*. Mat. Zametki (2006), 384-395.
> - [PALOMAR-2026-10-12-000005](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-12-000005&version=1)

*Quoted from [FormalConjectures/ErdosProblems/1180.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1180](https://www.erdosproblems.com/1180).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos1180.erdos_1180`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1180.lean#L1249](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1180.lean#L1249).

> Let $\epsilon>0$. Does there exist a constant $C_\epsilon$ such that, for all primes $p$, every
> residue modulo $p$ is the sum of at most $C_\epsilon$ many elements of
>
> $$\{ n^{-1} : 1\leq n\leq p^\epsilon\}$$
>
> where $n^{-1}$ denotes the inverse of $n$ modulo $p$?
>
> The original question was answered in the affirmative by Shparlinski [Sh02], who proved that
> $\ll \epsilon^{-3}$ summands suffice for all sufficiently large primes. This was improved to
> $\ll \epsilon^{-2}$ by Glibichuk [Gl06]. It is trivial that at least $\gg \epsilon^{-1}$
> summands are required, and it may be that $C_\epsilon\leq \epsilon^{-1-o(1)}$ is possible.
>
> See also [540](https://www.erdosproblems.com/540).

```lean
theorem erdos_1180 : ∀ ε : ℝ, 0 < ε → ∃ C : ℕ, ∀ p : ℕ, p.Prime → ∀ a : ZMod p,
    ∃ s : Multiset ℕ, s.card ≤ C ∧ Represents ε p a s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1180.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean#L71).

## `Erdos1180.erdos_1180.variants.shparlinski`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L89](https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L89).

> Shparlinski [Sh02] proved that $\ll \epsilon^{-3}$ summands suffice for every residue modulo
> every sufficiently large prime, where the threshold on $p$ may depend on $\epsilon$. No bound
> polynomial in $\epsilon^{-1}$ can hold for all primes, since when $p^\epsilon < 2$ the only
> admissible denominator is $1$.

```lean
theorem erdos_1180.variants.shparlinski : ∃ K : ℝ, ∀ ε : ℝ, 0 < ε → ε ≤ 1 →
    ∃ P : ℕ, ∀ p : ℕ, P ≤ p → p.Prime → ∀ a : ZMod p,
      ∃ s : Multiset ℕ, (s.card : ℝ) ≤ K * ε⁻¹ ^ 3 ∧ Represents ε p a s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1180.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean#L84).

## `Erdos1180.erdos_1180.variants.glibichuk`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L83](https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L83).

> Glibichuk [Gl06] improved the bound to $\ll \epsilon^{-2}$ summands, again for every
> sufficiently large prime.

```lean
theorem erdos_1180.variants.glibichuk : ∃ K : ℝ, ∀ ε : ℝ, 0 < ε → ε ≤ 1 →
    ∃ P : ℕ, ∀ p : ℕ, P ≤ p → p.Prime → ∀ a : ZMod p,
      ∃ s : Multiset ℕ, (s.card : ℝ) ≤ K * ε⁻¹ ^ 2 ∧ Represents ε p a s
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1180.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean#L96).

## `Erdos1180.erdos_1180.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L95](https://github.com/linrock/math-proofs/blob/ba96303b34a95ac458958c1eb0bbdee54733484a/erdos-1180/Solution.lean#L95).

> It is trivial that at least $\gg \epsilon^{-1}$ summands are required.

```lean
theorem erdos_1180.variants.lower_bound : ∃ K : ℝ, 0 < K ∧ ∀ ε : ℝ, 0 < ε → ε ≤ 1 →
    K * ε⁻¹ ≤ C ε
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1180.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean#L105).

## `Erdos1180.erdos_1180.variants.optimal`

Open: stated without proof.

> Is $C_\epsilon\leq \epsilon^{-1-o(1)}$? Here $C_\epsilon$ is the number of summands needed for
> every sufficiently large prime, as in `erdos_1180.variants.shparlinski` and
> `erdos_1180.variants.glibichuk`. For all primes no such bound holds, since when $p^\epsilon < 2$
> the only admissible denominator is $1$.

```lean
theorem erdos_1180.variants.optimal : ∀ δ : ℝ, 0 < δ →
    ∀ᶠ ε : ℝ in nhdsWithin 0 (Set.Ioi 0), ∃ P : ℕ, ∀ p : ℕ, P ≤ p → p.Prime → ∀ a : ZMod p,
      ∃ s : Multiset ℕ, (s.card : ℝ) ≤ ε⁻¹ ^ (1 + δ) ∧ Represents ε p a s
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1180.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1180.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1180.lean)
- [erdosproblems.com/1180](https://www.erdosproblems.com/1180)
