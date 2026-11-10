---
declaration: section
origin: cited
lean: Algebra.TensorProduct.isNoetherianRing_and_isCohenMacaulay_of_essFiniteType, Algebra.TensorProduct.isMaximalCohenMacaulay_self_iff_of_essFiniteType
statement: formalized
proof: formalized
---

# 10.167 Geometrically Cohen-Macaulay algebras

Section 10.167 of the Stacks Project, [Tag 045L](https://stacks.math.columbia.edu/tag/045L). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 045M, a lemma

[Tag 045M](https://stacks.math.columbia.edu/tag/045M) in the Stacks Project.

**`Algebra.TensorProduct.isNoetherianRing_and_isCohenMacaulay_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/FieldExtension.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/FieldExtension.lean#L403). The attribute's comment: “Finite generation of a field extension is `Algebra.EssFiniteType` (`IntermediateField.fg_top_iff`), and "one of them" is the disjunction `h`. Cohen-Macaulayness of the ring (Definition 00NC) is `Module.IsCohenMacaulay R R` for `R = K ⊗[k] L`, the notion of tag 0AAH for `R` over itself, which at each prime is Cohen-Macaulayness of `R_𝔭`. See the module docstring.”. References: EGA IV (6.7.1.1).

> **Stacks 045M.** Let `k` be a field and let `K/k` and `L/k` be field extensions one of which
> is of finite type as a field extension. Then `K ⊗[k] L` is a Noetherian Cohen–Macaulay ring.

```lean
public theorem Algebra.TensorProduct.isNoetherianRing_and_isCohenMacaulay_of_essFiniteType
    (k K L : Type*) [Field k] [Field K] [Field L] [Algebra k K] [Algebra k L]
    (h : Algebra.EssFiniteType k K ∨ Algebra.EssFiniteType k L) :
    IsNoetherianRing (K ⊗[k] L) ∧ Module.IsCohenMacaulay (K ⊗[k] L) (K ⊗[k] L)
```

## Tag 045N, a lemma

[Tag 045N](https://stacks.math.columbia.edu/tag/045N) in the Stacks Project.

**`Algebra.TensorProduct.isMaximalCohenMacaulay_self_iff_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/FieldExtension.lean, line 772](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/FieldExtension.lean#L772). The attribute's comment: “Cohen-Macaulayness of a Noetherian local ring (Definition 00N8) is `Module.IsMaximalCohenMacaulay A A` (Tag 00NF); finite generation of the field extension is `Algebra.EssFiniteType k K` (`IntermediateField.fg_top_iff`), as in Tag 045M; both localisations are abstract `IsLocalization.AtPrime`s as in Tag 00ND; lying over is contraction along `Algebra.TensorProduct.includeRight`, there being no `Algebra S (K ⊗[k] S)` instance; and `IsNoetherianRing (K ⊗[k] S)` is not assumed, being a consequence by Tag 045I. See the module docstring.”. References: EGA IV (6.7.1), “(i), CM, affine”; EGA IV (6.7.1.1), “more general”.

> **Stacks 045N.** Let `k` be a field, `S` a Noetherian `k`-algebra and `K/k` a finitely
> generated field extension. Let `𝔮 ⊆ S` be a prime and let `𝔮_K ⊆ K ⊗[k] S` be a prime lying over
> it along `s ↦ 1 ⊗ s`. Then the local ring `S_𝔮` is Cohen–Macaulay, that is
> `depth_{𝔪}(S_𝔮) = dim S_𝔮`, if and only if the local ring `(K ⊗[k] S)_{𝔮_K}` is.

```lean
public theorem Algebra.TensorProduct.isMaximalCohenMacaulay_self_iff_of_essFiniteType
    {k S : Type*} [Field k] [CommRing S] [Algebra k S] [IsNoetherianRing S]
    {K : Type*} [Field K] [Algebra k K] [Algebra.EssFiniteType k K]
    (q : Ideal S) [q.IsPrime] (qK : Ideal (K ⊗[k] S)) [qK.IsPrime]
    (hqK : q = qK.comap Algebra.TensorProduct.includeRight.toRingHom)
    (Sq : Type*) [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q] [IsLocalRing Sq]
    (SKqK : Type*) [CommRing SKqK] [Algebra (K ⊗[k] S) SKqK]
    [IsLocalization.AtPrime SKqK qK] [IsLocalRing SKqK] :
    Module.IsMaximalCohenMacaulay Sq Sq ↔ Module.IsMaximalCohenMacaulay SKqK SKqK
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.167, Tag 045L](https://stacks.math.columbia.edu/tag/045L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
