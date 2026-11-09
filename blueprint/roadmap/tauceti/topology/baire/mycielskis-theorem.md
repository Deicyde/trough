---
declaration: theorem
origin: cited
lean: TauCeti.mycielski, TauCeti.mycielski_prod
statement: formalized
proof: formalized
---

# Mycielski's theorem

Let `X` be a nonempty perfect completely metrizable space, for
example a nonempty perfect Polish space, and let `R n` be a meagre set of `k n`-tuples of points
of `X` for each `n`. There is a continuous injection `f` of Cantor space into `X` such that for
every `n` and every injective tuple `a` of `k n` points of Cantor space, `f ∘ a ∉ R n`.

```lean
TauCeti.mycielski.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.IsCompletelyMetrizableSpace X] [PerfectSpace X] [Nonempty X] (k : ℕ → ℕ)
  (R : (n : ℕ) → Set (Fin (k n) → X)) (hR : ∀ (n : ℕ), IsMeagre (R n)) :
  ∃ f,
    Continuous f ∧
      Function.Injective f ∧
        ∀ (n : ℕ) (a : Fin (k n) → ℕ → Bool), Function.Injective a → f ∘ a ∉ R n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mycielski`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/Mycielski.html#TauCeti.mycielski).

## Other forms

**Mycielski's theorem, binary case.** Formalized in Tau Ceti as [`TauCeti.mycielski_prod`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/Mycielski.html#TauCeti.mycielski_prod).

```lean
TauCeti.mycielski_prod.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.IsCompletelyMetrizableSpace X] [PerfectSpace X] [Nonempty X] {M : Set (X × X)}
  (hM : IsMeagre M) :
  ∃ f, Continuous f ∧ Function.Injective f ∧ ∀ (x y : ℕ → Bool), x ≠ y → (f x, f y) ∉ M
```

## Sources

- [Tau Ceti documentation: `TauCeti.mycielski`](https://taucetiproject.org/docs/TauCeti/Topology/Baire/Mycielski.html#TauCeti.mycielski)
- [Source of `TauCeti.mycielski` in TauCeti/Topology/Baire/Mycielski.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Baire/Mycielski.lean#L161)
