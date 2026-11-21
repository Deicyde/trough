---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyConfluent_eta
statement: formalized
proof: formalized
---

# η-confluence for the λ-calculus

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullEtaConfluence`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean), by Maximiliano Onofre Martínez.

> ## Reference
>
> * [T. Nipkow, *More Church-Rosser Proofs (in Isabelle/HOL)*][Nipkow2001]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyConfluent_eta` (lemma, [line 38](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean#L38))

```lean
lemma stronglyConfluent_eta : StronglyConfluent (@FullEta Var)
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [η-reduction for the λ-calculus](fulleta.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullEtaConfluence.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullEtaConfluence.json)
