---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.hodgeToDeRhamFirstPage
statement: formalized
proof: formalized
---

# 50.6 Two spectral sequences

Section 50.6 of the Stacks Project, [Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FM6, the section

[Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeToDeRhamFirstPage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRham.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeFiltration/HodgeToDeRham.lean#L95). The attribute's comment: “the first page of the Hodge-to-de Rham spectral sequence, E\_1^\{p,q} = H^q(X, Ω^p) with d\_1 induced by the de Rham differential; the spectral sequence itself and the conjugate spectral sequence are not constructed”. References: SGA 7 XXII (3.3), “First page of (3.3.2)”.

> **The `q`-th row `E_1^{•, q}` of the first page of the Hodge-to-de Rham spectral sequence of
> Stacks Section 0FM6.** The term in position `p` is the Hodge cohomology group
> `H^q(X, Ω^p_{𝒪_X/A})` and the differential `d_1^{p, q} : H^q(X, Ω^p) ⟶ H^q(X, Ω^{p + 1})` is the
> map induced by the de Rham differential `d : Ω^p ⟶ Ω^{p + 1}`; it squares to zero because the de
> Rham differential does.

```lean
abbrev hodgeToDeRhamFirstPage (q : ℕ) : CochainComplex AddCommGrpCat.{u} ℕ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.6, Tag 0FM6](https://stacks.math.columbia.edu/tag/0FM6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
