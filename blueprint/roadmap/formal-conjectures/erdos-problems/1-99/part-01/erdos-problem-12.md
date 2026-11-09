---
declaration: theorem
origin: cited
lean: Erdos12.isGood_example, Erdos12.erdos_12.parts.i, Erdos12.erdos_12.parts.ii, Erdos12.erdos_12.parts.iii, Erdos12.erdos_12.variants.erdos_sarkozy_density_0, Erdos12.erdos_12.variants.erdos_sarkozy, Erdos12.erdos_12.variants.example, Erdos12.erdos_12.variants.schoen, Erdos12.erdos_12.variants.baier
statement: formalized
---

# Erdős Problem 12

> *Reference:* [erdosproblems.com/12](https://www.erdosproblems.com/12)

*Quoted from [FormalConjectures/ErdosProblems/12.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/12](https://www.erdosproblems.com/12).

The file states 9 research or textbook statements: 1 open, 7 solved and 1 textbook result.

## `Erdos12.isGood_example`

Textbook result, stated without proof. A Lean proof is at [https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/ErdosProblems/12.lean#L39](https://github.com/mo271/formal-conjectures/blob/2663234a28260853790aa5752d8d4550ff0ab1ca/FormalConjectures/ErdosProblems/12.lean#L39).

> The set of $p ^ 2$ where $p \cong 3 \mod 4$ is prime is an example of a good set.
> Formal proof provided by AlphaProof

```lean
theorem isGood_example :
    IsGood {p ^ 2 | (p : ℕ) (_ : p ≡ 3 [MOD 4]) (_ : p.Prime)}
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L45).

## `Erdos12.erdos_12.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/8d872b465955e46e2d28bc165d186ea41fd0da9e/FormalConjectures/ErdosProblems/12.lean#L810](https://github.com/mo271/formal-conjectures/blob/8d872b465955e46e2d28bc165d186ea41fd0da9e/FormalConjectures/ErdosProblems/12.lean#L810).

> Let $A$ be an infinite set such that there are no distinct $a,b,c \in A$
> such that $a \mid (b+c)$ and $b,c > a$. Is there such an $A$ with
> $\liminf \frac{|A \cap \{1, \dotsc, N\}|}{N^{1/2}} > 0$ ?
>
> The DeepMind prover agent has found a formal proof of this statement.

```lean
theorem erdos_12.parts.i : ∃ (A : Set ℕ), IsGood A ∧
    (0 : ℝ) < Filter.atTop.liminf
      (fun N => (A ∩ Icc 1 N).ncard / (N : ℝ).sqrt)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L62).

## `Erdos12.erdos_12.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/118a6a60df73a9f47d6c89f3cdb3786eaa2e8d0a/FormalConjectures/ErdosProblems/12.lean#L740](https://github.com/mo271/formal-conjectures/blob/118a6a60df73a9f47d6c89f3cdb3786eaa2e8d0a/FormalConjectures/ErdosProblems/12.lean#L740).

> Let $A$ be an infinite set such that there are no distinct $a,b,c \in A$
> such that $a \mid (b+c)$ and $b,c > a$. Does there exist some absolute constant $c > 0$
> such that there are always infinitely many $N$
> with $|A \cap \{1, \dotsc, N\}| < N^{1−c}$?
>
> The DeepMind prover agent has found a formal disproof of this statement.

```lean
theorem erdos_12.parts.ii : ¬ ∃ c > (0 : ℝ), ∀ (A : Set ℕ), IsGood A →
    {N : ℕ| (A ∩ Icc 1 N).ncard < (N : ℝ) ^ (1 - c)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L78).

## `Erdos12.erdos_12.parts.iii`

Open: stated without proof.

> Let $A$ be an infinite set such that there are no distinct $a,b,c \in A$
> such that $a \mid (b+c)$ and $b,c > a$. Is it true that $∑_{n \in A} \frac{1}{n} < \infty$?

```lean
theorem erdos_12.parts.iii :
    ∀ (A : Set ℕ), IsGood A → Summable (fun (n : A) ↦ (1 / n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L87).

## `Erdos12.erdos_12.variants.erdos_sarkozy_density_0`

Solved: stated here without proof.

> Erdős and Sárközy proved that such an $A$ must have density 0.
> [ErSa70] Erd\H os, P. and Sárk\"ozi, A., On the divisibility properties of sequences of integers.
>     Proc. London Math. Soc. (3) (1970), 97-101

```lean
theorem erdos_12.variants.erdos_sarkozy_density_0 (A : Set ℕ) (hA : IsGood A) : A.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L97).

## `Erdos12.erdos_12.variants.erdos_sarkozy`

Solved: stated here without proof.

> Given any function $f(x)\to \infty$ as $x\to \infty$ there exists a set $A$ with the property
> that there are no distinct $a,b,c \in A$ such that $a \mid (b+c)$ and $b,c > a$, such that there are
> infinitely many $N$ such that $$\lvert A\cap\{1,\ldots,N\}\rvert > \frac{N}{f(N)}.

```lean
theorem erdos_12.variants.erdos_sarkozy (f : ℕ → ℕ) (hf : atTop.Tendsto f atTop) :
    ∃ A, IsGood A ∧ {N : ℕ | (N : ℝ) / f N < (A ∩ Icc 1 N).ncard}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L106).

## `Erdos12.erdos_12.variants.example`

Solved: stated here without proof.

> An example of an $A$ with the property that there are no distinct $a,b,c \in A$ such that
> $a \mid (b+c)$ and $b,c > a$ and such that
>
> $$\liminf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}\log N > 0$$
>
> is given by the set of $p^2$, where $p\equiv 3\pmod{4}$ is prime.

```lean
theorem erdos_12.variants.example (A : Set ℕ)
    (hA : A = {p ^ 2 | (p : ℕ) (_ : p.Prime) (_ : p ≡ 3 [MOD 4])}) :
    IsGood A ∧ 0 < atTop.liminf (fun (N : ℕ) ↦ (A ∩ Icc 1 N).ncard * (N : ℝ).log / √N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L117).

## `Erdos12.erdos_12.variants.schoen`

Solved: stated here without proof.

> Let $A$ be a set of natural numbers with the property that there are no distinct $a,b,c \in A$ such
> that $a \mid (b+c)$ and $b,c > a$. If all elements in $A$ are pairwise coprime then
>
> $$\lvert A\cap\{1,\ldots,N\}\rvert \ll N^{2/3}$$
>
> for infinitely many $N$.

```lean
theorem erdos_12.variants.schoen (A : Set ℕ) (hA : IsGood A) (hA' : A.Pairwise Nat.Coprime) :
    ∃ C > (0 : ℝ), {N : ℕ | (A ∩ Icc 1 N).ncard ≤ C * (N : ℝ) ^ (2 / 3 : ℝ)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L130).

## `Erdos12.erdos_12.variants.baier`

Solved: stated here without proof.

> Let $A$ be a set of natural numbers with the property that there are no distinct $a,b,c \in A$ such
> that $a \mid (b+c)$ and $b,c > a$. If all elements in $A$ are pairwise coprime then
>
> $$\lvert A\cap\{1,\ldots,N\}\rvert \ll N^{2/3}/\log N$$
>
> for infinitely many $N$.

```lean
theorem erdos_12.variants.baier (A : Set ℕ) (hA : IsGood A) (hA' : A.Pairwise Nat.Coprime) :
    ∃ C > (0 : ℝ),
      {N : ℕ | (A ∩ Icc 1 N).ncard ≤ C * (N : ℝ) ^ (2 / 3 : ℝ) / (N : ℝ).log}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/12.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/12.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/12.lean)
- [erdosproblems.com/12](https://www.erdosproblems.com/12)
