---
declaration: theorem
origin: cited
lean: Erdos402.erdos_402, Erdos402.erdos_402.variants.equality, Erdos402.erdos_402.variants.szegedy_zaharescu_weak
statement: formalized
---

# Erdős Problem 402

> *Reference:* [erdosproblems.com/402](https://www.erdosproblems.com/402)

*Quoted from [FormalConjectures/ErdosProblems/402.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/402.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/402](https://www.erdosproblems.com/402).

The file states 3 research or textbook statements: 3 solved.

## `Erdos402.erdos_402`

Solved: stated here without proof.

> Prove that, for any finite set $A\subset\mathbb{N}$, there exist $a, b\in A$ such
> that
>
> $$
>   \gcd(a, b)\leq a/|A|.
> $$

```lean
theorem erdos_402 (A : Finset ℕ) (h₁ : 0 ∉ A) (h₂ : A.Nonempty) : ∃ᵉ (a ∈ A) (b ∈ A),
    a.gcd b ≤ (a / A.card : ℚ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/402.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/402.lean#L38).

## `Erdos402.erdos_402.variants.equality`

Solved: stated here without proof.

> A conjecture of Graham [Gr70], who also conjectured that (assuming $A$ itself
> has no common divisor) the only cases where equality is achieved are when
> $A = \{1, \dots, n\}$ or $A = \{L/1, \dots, L/n\}$ (where $L = \operatorname{lcm}(1, \dots, n)$) or
> $A = \{2, 3, 4, 6\}$.
> Note: The source [BaSo96] mentioned on the Erdős page makes it clear what
> quantifiers to use for "where equality is achieved". See Theorem 1.1 there.
>
> TODO(firsching): Consider if we should have the other direction here as well or
> an iff statement.

```lean
theorem erdos_402.variants.equality (A : Finset ℕ) (h₁ : 0 ∉ A) (h₂ : A.Nonempty)
    (h₃ : A.gcd id = 1)
    (h : ∀ᵉ (a ∈ A) (b ∈ A), (a / A.card : ℚ) ≤ a.gcd b) :
    A = Finset.Icc 1 A.card ∨
    A = (Finset.Icc 1 A.card).image ((Finset.Icc 1 A.card).lcm id / ·) ∨
    A = {2, 3, 4, 6}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/402.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/402.lean#L53).

## `Erdos402.erdos_402.variants.szegedy_zaharescu_weak`

Solved: stated here without proof.

> Proved for all sufficiently large sets (including the sharper version which
> characterises the case of equality) independently by Szegedy [Sz86] and
> Zaharescu [Za87]. The following is taken from [Sz86].
>
> There exists an effectively computable $n_0$ with the following properties:
> (i) if $n \ge n_0$ and $a_1, a_2, \dots, a_n$ are distinct natural numbers then
> $\max_{i, j} \frac{a_i}{(a_i, a_j)} \ge n$.
> (ii) If equality holds then the system $\{a_1, a_2, \dots, a_n\}$ is either of the
> type $\{k, 2k, \dots, nk\}$ or of the type
> $\left\{\frac{k}{1}, \frac{k}{2}, \dots, \frac{k}{n}\right\}$.

```lean
theorem erdos_402.variants.szegedy_zaharescu_weak : ∀ᶠ n in atTop,
    ∀ (A : Finset ℕ), A.card = n → 0 ∉ A →
      (n ≤ (A ×ˢ A).sup (fun x => x.1 / x.1.gcd x.2)) ∧
      (n = (A ×ˢ A).sup (fun x => x.1 / x.1.gcd x.2) ↔
        ∃ k > 0, A = (Finset.Icc 1 n).image (k * ·) ∨
          A = (Finset.Icc 1 n).image (k * (Finset.Icc 1 n).lcm id / ·))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/402.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/402.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/402.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/402.lean)
- [erdosproblems.com/402](https://www.erdosproblems.com/402)
