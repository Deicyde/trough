---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver
statement: formalized
proof: formalized
---

# 110.61 Sheaves on the category of Noetherian schemes

Section 110.61 of the Stacks Project, [Tag 0GE8](https://stacks.math.columbia.edu/tag/0GE8). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GE9, a lemma

[Tag 0GE9](https://stacks.math.columbia.edu/tag/0GE9) in the Stacks Project.

**`AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean#L416).

> **Stacks 0GE9.** *With `S = Spec 𝐅_p` the inclusion functor
> `(Noetherian/S)_{fppf} ⟶ (Sch/S)_{fppf}` does not define a morphism of sites.*
>
> Its pushforward on sheaves of sets has no left exact left adjoint. Both sites are subcanonical,
> so a left exact `u_s` would identify the two Yoneda embeddings and force the inclusion to
> preserve monomorphisms, which by
> `AlgebraicGeometry.LocallyNoetherianOver.not_preservesMonomorphisms_toBigFppfOver` it does
> not.

```lean
public theorem not_isMorphismOfSites_toBigFppfOver
    (p : ℕ) [Fact p.Prime] (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of (ULift.{u} (ZMod p))))) :
    ¬ IsMorphismOfSites.{u + 1}
      (toBigFppfOver B (Spec (.of (ULift.{u} (ZMod p)))) hS)
      (fppfTopology B (Spec (.of (ULift.{u} (ZMod p)))) hS)
      (BigFppfOver.topology B (Spec (.of (ULift.{u} (ZMod p)))) hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.61, Tag 0GE8](https://stacks.math.columbia.edu/tag/0GE8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
