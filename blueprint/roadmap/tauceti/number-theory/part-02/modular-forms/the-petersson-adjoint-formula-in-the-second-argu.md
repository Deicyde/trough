---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right
statement: formalized
proof: formalized
---

# The Petersson adjoint formula in the second argument

For `n` coprime to `N`,

`⟪f, Tₙ g⟫ = ⟪⟨n⟩⁻¹ Tₙ f, g⟫`.

This is the Hermitian transpose of
`peterssonInnerCosets_heckeTCuspNat_left`.

```lean
HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right {N n : ℕ} [NeZero N] [NeZero n] (k : ℤ)
  (hn : n.Coprime N)
  (f g :
    CuspForm (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) (CongruenceSubgroup.Gamma1 N)) k) :
  f.peterssonInnerCosets ((HeckeRing.GL2.heckeTCuspNat k n) g) =
    ((TauCeti.diamondOpCusp k (ZMod.unitOfCoprime n hn)⁻¹)
          ((HeckeRing.GL2.heckeTCuspNat k n) f)).peterssonInnerCosets
      g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's decomposition of a double coset into right cosets](../hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Petersson/Normal.html#HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Petersson/Normal.html#HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right)
- [Source of `HeckeRing.GL2.peterssonInnerCosets_heckeTCuspNat_right` in TauCeti/NumberTheory/ModularForms/Petersson/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Petersson/Normal.lean#L80)
