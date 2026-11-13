---
declaration: theorem
origin: cited
lean: Kaplansky.zero_divisor_conjecture, Kaplansky.idempotent_conjecture, Kaplansky.UnitConjecture.counterexamples.i, Kaplansky.UnitConjecture.counterexamples.ii, Kaplansky.counter_unit_conjecture, Kaplansky.counter_unit_conjecture_weak, Kaplansky.counter_zero_divisor_conjecture
statement: formalized
---

# Kaplansky's Conjectures

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures)
> * [OAI26a] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*. OpenAI Math Release
>   preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf
>
> Throughout, "torsion-free" means that the identity is the only element of finite order
> (`Monoid.IsTorsionFree`). This is weaker than Mathlib's `IsMulTorsionFree`, which asks for
> uniqueness of roots and fails for the Promislow group below.

*Quoted from [FormalConjectures/Wikipedia/Kaplansky.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 2 API statements, counted here but not shown.

## `Kaplansky.zero_divisor_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/GroupRing/Main.lean#L13](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/GroupRing/Main.lean#L13).

> **The zero-divisor conjecture**
>
> If `G` is torsion-free, then the group algebra `K[G]` has no non-trivial zero divisors.
>
> This is false. It was disproved by an internal OpenAI model in September 2026 [OAI26a], which
> constructed a finitely presented torsion-free group $G$ and non-zero
> $\alpha, \beta \in \mathbb{F}_2[G]$ with $\alpha \beta = 0$; see
> `counter_zero_divisor_conjecture` and the linked Lean proof.

```lean
theorem zero_divisor_conjecture :
    ¬ ∀ (K : Type) [Field K] (G : Type) [Group G], Monoid.IsTorsionFree G →
      NoZeroDivisors (MonoidAlgebra K G)
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L56).

## `Kaplansky.idempotent_conjecture`

Open: stated without proof.

> **The idempotent conjecture**
>
> If `G` is torsion-free, then `K[G]` has no non-trivial idempotents.

```lean
theorem idempotent_conjecture (a : MonoidAlgebra K G) (h : IsIdempotentElem a) :
    a = 0 ∨ a = 1
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L67).

## `Kaplansky.UnitConjecture.counterexamples.i`

Solved: stated here without proof.

> If $P$ is the Promislow group, then the group ring $\mathbb{F}_p[P]$ has a non-trivial unit.

```lean
theorem UnitConjecture.counterexamples.i (p : ℕ) [hp : Fact p.Prime] :
    ∃ (u : (MonoidAlgebra (ZMod p) PromislowGroup)ˣ), ¬IsTrivialUnit u.val
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L109).

## `Kaplansky.UnitConjecture.counterexamples.ii`

Solved: stated here without proof.

> If $P$ is the Promislow group, then the group ring $\mathbb{C}[P]$ has a non-trivial unit.

```lean
theorem UnitConjecture.counterexamples.ii :
    ∃ (u : (MonoidAlgebra ℂ PromislowGroup)ˣ), ¬IsTrivialUnit u.val
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L117).

## `Kaplansky.counter_unit_conjecture`

Proved here.

> The **Unit Conjecture** is false.
>
> At least there is a counterexample for any prime and zero characteristic:
> [Mu21] Murray, A. (2021). More Counterexamples to the Unit Conjecture for Group Rings.
> [Pa21] Passman, D. (2021). On the counterexamples to the unit conjecture for group rings.
> [Ga24] Gardam, G. (2024). Non-trivial units of complex group rings.

```lean
theorem counter_unit_conjecture :
    ∃ (G : Type) (_ : Group G) (_ : Monoid.IsTorsionFree G),
    ∀ (p : ℕ) (_ : p = 0 ∨ p.Prime),
    ∃ (K : Type) (_ : Field K) (_ :  CharP K p) (u : (MonoidAlgebra K G)ˣ), ¬IsTrivialUnit u.val
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L130).

## `Kaplansky.counter_unit_conjecture_weak`

Proved here.

> There is a counterexample to **Unit Conjecture** in any characteristic.

```lean
theorem counter_unit_conjecture_weak (p : ℕ) (hp : p = 0 ∨ p.Prime) :
    ∃ (G : Type) (_ : Group G) (_ : Monoid.IsTorsionFree G)
      (K : Type) (_ : Field K) (_ :  CharP K p) (u : (MonoidAlgebra K G)ˣ), ¬IsTrivialUnit u.val
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L142).

## `Kaplansky.counter_zero_divisor_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/GroupRing/Main.lean#L13](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/GroupRing/Main.lean#L13).

> The **Zero-divisor Conjecture** is false: there is a finitely presented torsion-free group $G$
> and non-zero $\alpha, \beta \in \mathbb{F}_2[G]$ with $\alpha \beta = 0$.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
theorem counter_zero_divisor_conjecture :
    ∃ (G : Type) (_ : Group G) (_ : Monoid.IsTorsionFree G) (_ : Group.IsFinitelyPresented G)
      (α β : MonoidAlgebra (ZMod 2) G), α ≠ 0 ∧ β ≠ 0 ∧ α * β = 0
```

Category `research solved`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/Kaplansky.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean#L158).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Kaplansky.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Kaplansky.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures)
