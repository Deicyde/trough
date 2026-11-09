---
declaration: theorem
origin: cited
lean: Erdos358.f_id, Erdos358.erdos_358.parts.i, Erdos358.erdos_358.parts.ii, Erdos358.erdos_358.variants.prime_set, Erdos358.erdos_358.variants.prime_set_density_representation, Erdos358.erdos_358.variants.one_le
statement: formalized
---

# Erdős Problem 358

> *References:*
> - [erdosproblems.com/358](https://www.erdosproblems.com/358)
> - [Ta26] T. Tao, [Erdős problem 358](https://terrytao.wordpress.com/wp-content/uploads/2026/02/erdos-358-2.pdf) (2026)

*Quoted from [FormalConjectures/ErdosProblems/358.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/358](https://www.erdosproblems.com/358).

The file states 6 research or textbook statements: 2 open, 3 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos358.f_id`

Textbook result, stated without proof.

> When $A_n = n$, the function $f$ defined above counts the number of odd divisors of $n$.

```lean
theorem f_id : f id = fun n ↦ #{d ∈ n.divisors | Odd d}
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L66).

## `Erdos358.erdos_358.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos358.lean#L9111](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos358.lean#L9111).

> Let $A=\{a_1 < \cdots\}$ be an infinite sequence of integers. Let $f(n)$ count the number of
> solutions to
>
> $$n=\sum_{u\leq i\leq v}a_i.$$
>
> Is there such an $A$ for which $f(n)\to \infty$ as $n\to \infty$?
>
> Tao [Ta26] constructed such a sequence with $f(n) \gg \log n$ for all sufficiently large $n$.

```lean
theorem erdos_358.parts.i :
    ∃ A, StrictMono A ∧ atTop.Tendsto (f A) atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L78).

## `Erdos358.erdos_358.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos358.lean#L9115](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos358.lean#L9115).

> Let $A=\{a_1 < \cdots\}$ be an infinite sequence of integers. Let $f(n)$ count the number of
> solutions to
>
> $$n=\sum_{u\leq i\leq v}a_i.$$
>
> Is there an $A$ such that $f(n)\geq 2$ for all large $n$?
>
> This also follows from Tao's construction with $f(n) \gg \log n$ [Ta26].

```lean
theorem erdos_358.parts.ii :
    ∃ A, StrictMono A ∧ ∀ᶠ n in atTop, 2 ≤ f A n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L91).

## `Erdos358.erdos_358.variants.prime_set`

Open: stated without proof.

> When $A =\{a_1 < \cdots\}$ corresponds to the set of primes, it is conjectured that the
> $\limsup$ of the number of representations
>
> $$n=\sum_{u\leq i\leq v}a_i$$
>
> is infinite.

```lean
theorem erdos_358.variants.prime_set :
    atTop.limsup (fun n ↦ (f (Nat.nth Nat.Prime) n : ℕ∞)) = ⊤
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L100).

## `Erdos358.erdos_358.variants.prime_set_density_representation`

Open: stated without proof.

> When $A =\{a_1 < \cdots\}$ corresponds to the set of primes, it is conjectured that the set of
> numbers $n$ that have representations
>
> $$n=\sum_{u\leq i\leq v}a_i$$
>
> has positive upper density.

```lean
theorem erdos_358.variants.prime_set_density_representation :
    0 < {n : ℕ | intervalRepresentations (Nat.nth Nat.Prime) n |>.Nonempty}.upperDensity
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L109).

## `Erdos358.erdos_358.variants.one_le`

Proved here.

> In [ErGr80] Erdős and Graham further asked whether there is an $A$ with $f(n)\geq 1$ for all
> large $n$. Egami observed that this holds trivially for $a_n=n$, so they may have intended to
> count only those representations
>
> $$n=\sum_{u\leq i\leq v}a_i$$
>
> that use at least two consecutive
> terms, which is what $g$ counts.
>
> This follows from Tao's construction [Ta26], which gives $f(n)\gg\log n$: see
> `erdos_358.parts.ii` and `one_le_g_of_two_le_f`.

```lean
theorem erdos_358.variants.one_le :
    ∃ A, StrictMono A ∧ ∀ᶠ n in atTop, 1 ≤ g A n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/358.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean#L170).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/358.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/358.lean)
- [erdosproblems.com/358](https://www.erdosproblems.com/358)
