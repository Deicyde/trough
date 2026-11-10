---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleSchemeToSpace_isSpecialCocontinuous, AlgebraicGeometry.fppfSchemeToSpace_isSpecialCocontinuous, AlgebraicGeometry.phSchemeToSpace_isSpecialCocontinuous, AlgebraicGeometry.etaleSchemeToSpaceSheafEquiv, AlgebraicGeometry.fppfSchemeToSpaceSheafEquiv, AlgebraicGeometry.phSchemeToSpaceSheafEquiv
statement: formalized
proof: formalized
---

# 84.3 Transporting results from schemes

Section 84.3 of the Stacks Project, [Tag 0DFU](https://stacks.math.columbia.edu/tag/0DFU). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DFV, a lemma

[Tag 0DFV](https://stacks.math.columbia.edu/tag/0DFV) in the Stacks Project.

**`AlgebraicGeometry.etaleSchemeToSpace_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1216). The attribute's comment: “étale case”.

> **Stacks 0DFV, étale case.** The inclusion of schemes into algebraic
> spaces is special cocontinuous for the big étale sites.

```lean
public theorem etaleSchemeToSpace_isSpecialCocontinuous
    {S : Scheme.{u}} (T : AlgebraicGeometry.BigEtaleSpaceSite S)
    (h : T.schemeSite.cutoff = T.fppfSite.cutoff) :
    IsSpecialCocontinuous
      (AlgebraicGeometry.BigEtaleOver.topology T.schemeSite S T.scheme_mem)
      T.topology (etaleSchemeToSpace T h)
```

**`AlgebraicGeometry.fppfSchemeToSpace_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1233). The attribute's comment: “fppf case”.

> **Stacks 0DFV, fppf case.** The Yoneda inclusion of schemes into
> algebraic spaces is special cocontinuous for the big fppf sites.

```lean
public theorem fppfSchemeToSpace_isSpecialCocontinuous
    {S : Scheme.{u}} (T : AlgebraicGeometry.BigFppfSpaceSite S) :
    IsSpecialCocontinuous
      (AlgebraicGeometry.BigFppfOver.topology T.schemeSite S T.scheme_mem)
      T.topology
      (AlgebraicGeometry.schemeSpaceFunctor T.schemeSite S T.scheme_mem)
```

**`AlgebraicGeometry.phSchemeToSpace_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1261). The attribute's comment: “ph case”.

> **Stacks 0DFV, ph case.** The inclusion of schemes into algebraic
> spaces is special cocontinuous for the big ph sites.

```lean
public theorem phSchemeToSpace_isSpecialCocontinuous
    {S : Scheme.{u}} (T : AlgebraicGeometry.BigPHSpaceSite S) :
    IsSpecialCocontinuous
      (AlgebraicGeometry.BigPHOver.topology T.schemeSite S T.scheme_mem)
      T.topology T.schemeToSpace
```

**`AlgebraicGeometry.etaleSchemeToSpaceSheafEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1277). The attribute's comment: “étale case, equivalence of topoi”.

> **Stacks 0DFV, étale case: the identification of topoi.** The inclusion of schemes into
> algebraic spaces induces an equivalence between the big étale topos of the scheme site and the
> big étale topos of the algebraic-space site.

```lean
public noncomputable def etaleSchemeToSpaceSheafEquiv {S : Scheme.{u}}
    (T : AlgebraicGeometry.BigEtaleSpaceSite S)
    (h : T.schemeSite.cutoff = T.fppfSite.cutoff) :
    Sheaf (AlgebraicGeometry.BigEtaleOver.topology T.schemeSite S T.scheme_mem)
        (Type (u + 1)) ≌
      Sheaf T.topology (Type (u + 1))
```

**`AlgebraicGeometry.fppfSchemeToSpaceSheafEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1291). The attribute's comment: “fppf case, equivalence of topoi”.

> **Stacks 0DFV, fppf case: the identification of topoi.** The Yoneda inclusion of schemes
> into algebraic spaces induces an equivalence between the big fppf topos of the scheme site and
> the big fppf topos of the algebraic-space site.

```lean
public noncomputable def fppfSchemeToSpaceSheafEquiv {S : Scheme.{u}}
    (T : AlgebraicGeometry.BigFppfSpaceSite S) :
    Sheaf (AlgebraicGeometry.BigFppfOver.topology T.schemeSite S T.scheme_mem)
        (Type (u + 1)) ≌
      Sheaf T.topology (Type (u + 1))
```

**`AlgebraicGeometry.phSchemeToSpaceSheafEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean, line 1305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SchemeToSpaceSites.lean#L1305). The attribute's comment: “ph case, equivalence of topoi”.

> **Stacks 0DFV, ph case: the identification of topoi.** The inclusion of schemes into
> algebraic spaces induces an equivalence between the big ph topos of the scheme site and the
> big ph topos of the algebraic-space site.

```lean
public noncomputable def phSchemeToSpaceSheafEquiv {S : Scheme.{u}}
    (T : AlgebraicGeometry.BigPHSpaceSite S) :
    Sheaf (AlgebraicGeometry.BigPHOver.topology T.schemeSite S T.scheme_mem)
        (Type (u + 1)) ≌
      Sheaf T.topology (Type (u + 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.3, Tag 0DFU](https://stacks.math.columbia.edu/tag/0DFU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
