---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyCommute_eta_beta, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_beta_eta
statement: formalized
proof: formalized
---

# βη-Confluence for the λ-calculus (FullBetaEtaConfluence)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.FullBetaEtaConfluence`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean), by Maximiliano Onofre Martínez.

> ## Reference
>
> * [T. Nipkow, *More Church-Rosser Proofs (in Isabelle/HOL)*][Nipkow2001]

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.stronglyCommute_eta_beta` (lemma, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean#L38))

> η-reduction and β-reduction strongly commute.

```lean
lemma stronglyCommute_eta_beta : StronglyCommute (@FullEta Var) FullBeta
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.confluent_beta_eta` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean#L96))

> βη-reduction is confluent.

```lean
theorem confluent_beta_eta : Confluent (@FullBetaEta Var)
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [βη-Confluence for the λ-calculus (FullBetaEta)](fullbetaeta.md)

## Proof depends on

- [β-confluence for the λ-calculus](fullbetaconfluence.md)
- [η-confluence for the λ-calculus](fulletaconfluence.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/FullBetaEtaConfluence.lean)
