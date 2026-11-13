---
declaration: theorem
origin: cited
lean: Erdos723.erdos_723, Erdos723.erdos_723.variants.prime_power_is_projplane_order, Erdos723.erdos_723.variants.leq_11, Erdos723.erdos_723.variants.eq_12, Erdos723.erdos_723.variants.bruck_ryser
statement: formalized
---

# Erdős Problem 723: The prime power conjecture.

> *Reference:* [erdosproblems.com/723](https://www.erdosproblems.com/723)

*Quoted from [FormalConjectures/ErdosProblems/723.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/723](https://www.erdosproblems.com/723).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos723.erdos_723`

Open: stated without proof.

> If there is a finite projective plane of order $n$ then must $n$ be a prime power?

```lean
theorem erdos_723 :
    ∀ {P L : Type} (_: Membership P L) (_ : Fintype P) (_ : Fintype L),
      ∀ pp : ProjectivePlane P L, IsPrimePow pp.order
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/723.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean#L36).

## `Erdos723.erdos_723.variants.prime_power_is_projplane_order`

Solved: stated here without proof.

> These always exist if $n$ is a prime power.

```lean
theorem erdos_723.variants.prime_power_is_projplane_order :
    ∀ n, IsPrimePow n → ∃ (P L : Type) (_ : Membership P L) (_ : Fintype P) (_ : Fintype L)
      (pp : ProjectivePlane P L), pp.order = n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/723.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean#L45).

## `Erdos723.erdos_723.variants.leq_11`

Solved: stated here without proof.

> This conjecture has been proved for $n \leq 11$.

```lean
theorem erdos_723.variants.leq_11 {P L : Type} [Membership P L] [Fintype P] [Fintype L] :
    ∀ pp : ProjectivePlane P L, pp.order ≤ 11 → IsPrimePow pp.order
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/723.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean#L54).

## `Erdos723.erdos_723.variants.eq_12`

Open: stated without proof.

> It is open whether there exists a projective plane of order 12.

```lean
theorem erdos_723.variants.eq_12 :
    ∃ (P L : Type) (_ : Membership P L) (_ : Fintype P) (_ : Fintype L) (pp : ProjectivePlane P L),
      pp.order = 12
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/723.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean#L62).

## `Erdos723.erdos_723.variants.bruck_ryser`

Solved: stated here without proof.

> Bruck and Ryser have proved that if $n \equiv 1 (\mod 4)$ or $n \equiv 2 (\mod 4)$ then $n$ must be
> the sum of two squares.

```lean
theorem erdos_723.variants.bruck_ryser {P L : Type} [Membership P L] [Fintype P] [Fintype L]
    (n : ℕ) (pp : ProjectivePlane P L) (hpp : pp.order = n) :
    (n ≡ 1 [MOD 4] ∨ n ≡ 2 [MOD 4]) → ∃ a b, n = a ^ 2 + b ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/723.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/723.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/723.lean)
- [erdosproblems.com/723](https://www.erdosproblems.com/723)
