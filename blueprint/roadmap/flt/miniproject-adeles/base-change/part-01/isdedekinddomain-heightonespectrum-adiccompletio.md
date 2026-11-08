---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology
statement: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/326
---

# IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology

Giving $L_w$ the $K_v$-algebra structure coming from the natural map $K_v\to L_w$, the $w$-adic topology on $L_w$ is the $K_v$-module topology.

## Depends on

- [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom](isdedekinddomain-heightonespectrum-extension-adi.md)

## Proof

Any basis for $L$ as a $K$-vector space spans $L_w$ as a $K_v$-module, so $L_w$ is finite-dimensional over $K_v$ and the module topology is the same as the product topology. So we need to establish that the product topology on $L_w=K_v^n$ is the $w$-adic topology. But the $w$-adic topology is induced by the $w$-adic norm, which makes $L_w$ into a normed $K_v$-vector space, and (after picking a basis) the product norm on $L_w=K_v^n$ also makes $L_w$ into a normed $K_v$-vector space. So the result follows from the standard fact (see for example the lemma on p52 of Cassels-Froelich, formalized as ContinuousLinearEquiv.ofFinrankEq in mathlib) that any two norms on a finite-dimensional vector space over a complete field are equivalent (and thus induce the same topology).

## Lean

Stated as [`IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 203](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L203)
