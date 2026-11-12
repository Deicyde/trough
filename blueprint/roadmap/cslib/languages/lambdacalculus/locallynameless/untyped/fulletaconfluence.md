---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyConfluent_eta
statement: formalized
proof: formalized
---

# η-confluence for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullEtaConfluence`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean), by Maximiliano Onofre Martínez.

> ## Reference
>
> * [T. Nipkow, *More Church-Rosser Proofs (in Isabelle/HOL)*][Nipkow2001]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyConfluent_eta` (lemma, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean#L38))

```lean
lemma stronglyConfluent_eta : StronglyConfluent (@FullEta Var)
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [η-reduction for the λ-calculus](fulleta.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean)
