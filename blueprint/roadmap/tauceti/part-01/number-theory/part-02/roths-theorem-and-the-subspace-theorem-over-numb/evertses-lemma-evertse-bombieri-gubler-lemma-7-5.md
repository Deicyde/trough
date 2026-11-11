---
declaration: theorem
origin: cited
lean: NumberField.exists_evertse, NumberField.exists_evertse_unweighted
statement: formalized
proof: formalized
---

# Evertse's lemma (Evertse; Bombieri–Gubler, Lemma 7.5.29)

There is a constant `C`,
depending only on `K` and `m`, with the following property. Let `S₀` be a finite set of finite
places, `x` a basis of a `K`-vector space `V` indexed by `Fin m`, and at every infinite place and
every place of `S₀` let the forms `L v k` be linearly independent, the weights `ν v k` positive
and `μ v` nondecreasing, with `|L v k (x j)|_v ≤ ν v k * μ v j`. Then there are `ξ j l ∈ K`,
integral outside `S₀`, and permutations `π v`, such that `y j = x j + ∑ l < j, ξ j l • x l`
satisfies `|L v (π v i) (y j)|_v ≤ C * (ν v (π v i) * min (μ v i) (μ v j))` at every infinite
place and `|L v (π v i) (y j)|_v ≤ ν v (π v i) * min (μ v i) (μ v j)` at every place of `S₀`.

```lean
NumberField.exists_evertse.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K] (m : ℕ) :
  ∃ C,
    ∀ (V : Type u_2) [inst : AddCommGroup V] [inst_1 : _root_.Module K V]
      (Sfin : Finset (NumberField.FinitePlace K)) (L : AbsoluteValue K ℝ → Fin m → Module.Dual K V)
      (x : Module.Basis (Fin m) K V) (ν μ : AbsoluteValue K ℝ → Fin m → ℝ),
      (∀ (v : NumberField.InfinitePlace K), LinearIndependent K (L ↑v)) →
        (∀ v ∈ Sfin, LinearIndependent K (L ↑v)) →
          (∀ (v : NumberField.InfinitePlace K) (k : Fin m), 0 < ν (↑v) k) →
            (∀ v ∈ Sfin, ∀ (k : Fin m), 0 < ν (↑v) k) →
              (∀ (v : NumberField.InfinitePlace K), Monotone (μ ↑v)) →
                (∀ v ∈ Sfin, Monotone (μ ↑v)) →
                  (∀ (v : NumberField.InfinitePlace K) (k j : Fin m),
                      v ((L (↑v) k) (x j)) ≤ ν (↑v) k * μ (↑v) j) →
                    (∀ v ∈ Sfin, ∀ (k j : Fin m), v ((L (↑v) k) (x j)) ≤ ν (↑v) k * μ (↑v) j) →
                      ∃ ξ π,
                        (∀ (j l : Fin m), ∀ u ∉ Sfin, u (ξ j l) ≤ 1) ∧
                          (∀ (v : NumberField.InfinitePlace K) (i j : Fin m),
                              v ((L (↑v) ((π ↑v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
                                C * (ν (↑v) ((π ↑v) i) * min (μ (↑v) i) (μ (↑v) j))) ∧
                            ∀ v ∈ Sfin,
                              ∀ (i j : Fin m),
                                v ((L (↑v) ((π ↑v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
                                  ν (↑v) ((π ↑v) i) * min (μ (↑v) i) (μ (↑v) j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Evertse's lemma](../../../analysis/part-03/other-results/evertses-lemma.md)

## Lean

Formalized in Tau Ceti as [`NumberField.exists_evertse`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Approximation/Evertse.html#NumberField.exists_evertse).

## Other forms

**Evertse's lemma without weights (Evertse; Bombieri–Gubler, Lemma 7.5.29).** Formalized in Tau Ceti as [`NumberField.exists_evertse_unweighted`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Approximation/Evertse.html#NumberField.exists_evertse_unweighted).

```lean
NumberField.exists_evertse_unweighted.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K] (m : ℕ) :
  ∃ C,
    ∀ (V : Type u_2) [inst : AddCommGroup V] [inst_1 : _root_.Module K V]
      (Sfin : Finset (NumberField.FinitePlace K)) (L : AbsoluteValue K ℝ → Fin m → Module.Dual K V)
      (x : Module.Basis (Fin m) K V) (μ : AbsoluteValue K ℝ → Fin m → ℝ),
      (∀ (v : NumberField.InfinitePlace K), LinearIndependent K (L ↑v)) →
        (∀ v ∈ Sfin, LinearIndependent K (L ↑v)) →
          (∀ (v : NumberField.InfinitePlace K), Monotone (μ ↑v)) →
            (∀ v ∈ Sfin, Monotone (μ ↑v)) →
              (∀ (v : NumberField.InfinitePlace K) (k j : Fin m), v ((L (↑v) k) (x j)) ≤ μ (↑v) j) →
                (∀ v ∈ Sfin, ∀ (k j : Fin m), v ((L (↑v) k) (x j)) ≤ μ (↑v) j) →
                  ∃ ξ π,
                    (∀ (j l : Fin m), ∀ u ∉ Sfin, u (ξ j l) ≤ 1) ∧
                      (∀ (v : NumberField.InfinitePlace K) (i j : Fin m),
                          v ((L (↑v) ((π ↑v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
                            C * min (μ (↑v) i) (μ (↑v) j)) ∧
                        ∀ v ∈ Sfin,
                          ∀ (i j : Fin m),
                            v ((L (↑v) ((π ↑v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
                              min (μ (↑v) i) (μ (↑v) j)
```

## Sources

- [Tau Ceti documentation: `NumberField.exists_evertse`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Approximation/Evertse.html#NumberField.exists_evertse)
- [Source of `NumberField.exists_evertse` in TauCeti/NumberTheory/NumberField/Global/Approximation/Evertse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/Approximation/Evertse.lean#L62)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
