---
declaration: theorem
origin: cited
lean: LinearIsometry.exists_continuousLinearMap_of_doubleDual
statement: formalized
proof: formalized
---

# The principle of local reflexivity

Let `ι : V → E**` be a linear isometry from a
finite-dimensional normed space into the bidual of `E`, let `G` be a finite-dimensional subspace
of the dual of `E`, and let `ε > 0`. Then some continuous linear map `T : V → E` satisfies
`(1 - ε) ‖v‖ ≤ ‖T v‖ ≤ (1 + ε) ‖v‖`, preserves the pairing with `G` in the sense that
`g (T v) = ι v g` for `g ∈ G`, and inverts the canonical embedding on `V`: `T v = x` whenever
`ι v` is the canonical image of `x : E`.

```lean
LinearIsometry.exists_continuousLinearMap_of_doubleDual.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {V : Type u_3}
  [NormedAddCommGroup V] [NormedSpace 𝕜 V] [FiniteDimensional 𝕜 V]
  (ι : V →ₗᵢ[𝕜] StrongDual 𝕜 (StrongDual 𝕜 E)) (G : Submodule 𝕜 (StrongDual 𝕜 E))
  [FiniteDimensional 𝕜 ↥G] {ε : ℝ} (hε : 0 < ε) :
  ∃ T,
    (∀ (v : V), (1 - ε) * ‖v‖ ≤ ‖T v‖ ∧ ‖T v‖ ≤ (1 + ε) * ‖v‖) ∧
      (∀ (v : V), ∀ g ∈ G, g (T v) = (ι v) g) ∧
        ∀ (v : V) (x : E), ι v = (NormedSpace.inclusionInDoubleDual 𝕜 E) x → T v = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Helly's lemma](../part-02/hellys-lemma.md)

## Lean

Formalized in Tau Ceti as [`LinearIsometry.exists_continuousLinearMap_of_doubleDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.html#LinearIsometry.exists_continuousLinearMap_of_doubleDual).

## Sources

- [Tau Ceti documentation: `LinearIsometry.exists_continuousLinearMap_of_doubleDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.html#LinearIsometry.exists_continuousLinearMap_of_doubleDual)
- [Source of `LinearIsometry.exists_continuousLinearMap_of_doubleDual` in TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/LocalReflexivity.lean#L241)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
