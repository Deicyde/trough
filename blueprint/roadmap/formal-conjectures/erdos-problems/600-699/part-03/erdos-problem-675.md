---
declaration: theorem
origin: cited
lean: Erdos675.erdos_675.parts.i, Erdos675.erdos_675.parts.ii, Erdos675.erdos_675.parts.iii, Erdos675.erdos_675.variants.squarefree, Erdos675.erdos_675.variants.brun
statement: formalized
---

# Erdős Problem 675

> *References:*
> - [erdosproblems.com/675](https://www.erdosproblems.com/675)
> - [Er79] Erdős, Paul, *Some unconventional problems in number theory*. Math. Mag. (1979), 67-70.
> - [Ho26] Ho, B. S., *A squarefree lower bound for Erdős Problem 675*.
>   [PDF](https://boonsuan.github.io/erdos675_squarefree.pdf) (2026).

*Quoted from [FormalConjectures/ErdosProblems/675.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/675](https://www.erdosproblems.com/675).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 3 test statements, counted here but not shown.

## `Erdos675.erdos_675.parts.i`

Open: stated without proof.

> A set $A \subseteq \mathbb{N}$ has the translation property if, for every $n$, there is an
> integer $t_n \geq 1$ such that, for all $1 \leq a \leq n$, $a \in A$ if and only if
> $a + t_n \in A$. Does the set of sums of two squares $\{x^2 + y^2 : x, y \in \mathbb{N}\}$
> have the translation property?

```lean
theorem erdos_675.parts.i :
    HasTranslationProperty {m : ℕ | ∃ x y : ℕ, m = x ^ 2 + y ^ 2}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/675.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean#L97).

## `Erdos675.erdos_675.parts.ii`

Open: stated without proof.

> If we partition all primes into $P\sqcup Q$, such that each set contains $\gg x/\log x$ many
> primes $\leq x$ for all large $x$, then can the set of integers only divisible by primes from
> $P$ have the translation property?
>
> We read "can" as: is there such a partition for which this set (which contains $1$) has the
> translation property?

```lean
theorem erdos_675.parts.ii :
    ∃ P : Set ℕ, P ⊆ {p : ℕ | p.Prime} ∧
      (fun x : ℕ ↦ (x : ℝ) / Real.log x) =O[atTop] (fun x ↦ ((P ∩ Set.Iic x).ncard : ℝ)) ∧
      (fun x : ℕ ↦ (x : ℝ) / Real.log x) =O[atTop]
        (fun x ↦ ((({p : ℕ | p.Prime} \ P) ∩ Set.Iic x).ncard : ℝ)) ∧
      HasTranslationProperty (composedOf P)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/675.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean#L110).

## `Erdos675.erdos_675.parts.iii`

Solved: stated here without proof.

> If $A$ is the set of squarefree numbers then how fast does the minimal such $t_n$ grow? Is it
> true that $t_n>\exp(n^c)$ for some constant $c>0$?
>
> We ask for the inequality for all sufficiently large $n$, since $t_1 = 1$.
>
> Ho [Ho26] proved that the answer is yes: for every fixed $0 < c < 25/72$, $t_n > \exp(n^c)$ for
> all sufficiently large $n$ (Theorem 1.2 and Corollary 3.2); see also the
> [forum discussion](https://www.erdosproblems.com/forum/thread/675#post-6002).

```lean
theorem erdos_675.parts.iii :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      Real.exp ((n : ℝ) ^ c) < (minTranslation {m : ℕ | Squarefree m} n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/675.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean#L129).

## `Erdos675.erdos_675.variants.squarefree`

Solved: stated here without proof.

> Elementary sieve theory implies that the set of squarefree numbers has the translation property
> (as remarked on erdosproblems.com).

```lean
theorem erdos_675.variants.squarefree : HasTranslationProperty {m : ℕ | Squarefree m}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/675.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean#L139).

## `Erdos675.erdos_675.variants.brun`

Solved: stated here without proof.

> Let $B \subseteq \mathbb{N}$ be a set of pairwise coprime integers with
>
> $$\sum_{b \in B,\ b < x} \frac{1}{b} = o(\log \log x).$$
>
> Then $A = \{n : b \nmid n \text{ for all } b \in B\}$ has the translation property.
> As remarked on erdosproblems.com, this follows from Brun's sieve, and Erdős did not know what
> happens if the condition on the sum is weakened or dropped.

```lean
theorem erdos_675.variants.brun (B : Set ℕ) (hB : B.Pairwise Nat.Coprime)
    (hsum : (fun x : ℕ ↦ ∑ b ∈ Finset.range x with b ∈ B, (1 : ℝ) / (b : ℝ)) =o[atTop]
      fun x : ℕ ↦ Real.log (Real.log (x : ℝ))) :
    HasTranslationProperty {n : ℕ | ∀ b ∈ B, ¬ b ∣ n}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/675.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/675.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/675.lean)
- [erdosproblems.com/675](https://www.erdosproblems.com/675)
