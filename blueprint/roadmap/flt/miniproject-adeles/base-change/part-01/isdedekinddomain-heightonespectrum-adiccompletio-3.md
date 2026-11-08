---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv
statement: formalized
---

# IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv

The induced $L$-algebra homomorphism $L\otimes_KK_v\to\prod_{w|v}L_w$ is an isomorphism of rings.

## Depends on

- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.semialgHomPi](isdedekinddomain-heightonespectrum-adiccompletio-2.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.finite](isdedekinddomain-heightonespectrum-extension-fin.md)

## Proof

My current proposal to formalize this is as follows. The map is surjective because the image is dense and closed; this has been formalized already. It is also a $K_v$-algebra homomorphism if we give $L_w$ the obvious $K_v$-algebra structure. Thus we can conclude the result if we can prove that both spaces are finite-dimensional and have the same dimension. The $K_v$-dimension of $L\otimes_KK_v$ is equal to the $K$-dimension of $L$, which is $\sum_{w|v}e_wf_w$ using the standard notation that $e_w$ is the ramification index of $w$ and $f_w$ the residue degree (this result is in mathlib). So it suffices to prove that $[L_w:K_v]=e_wf_w$. We already have that $e_w$ (defined globally) is equal to the local ramification index (defined as the factor by which the valuations differ on $K$). So what is left is to prove that (i) the residue field extension induced by $L_w/K_v$ has degree is equal to the globally-defined $f_w$, (ii) an extension of local fields has degree $ef$. Now (i) sounds straightforward given what we have (the map from $A$ to $\mathcal{O}_v$ has kernel $v$ and dense image) and (ii) is true for any complete discretely-valued field; I am not suggesting we formalize the following proof, but at least it represents a rigorous justification: A field complete with respect to a discrete valuation is *stable* in the sense of the book by Bosch-Güntzer-Remmert (Prop 3.6.2.1), so every finite extension of such a field is cartesian (def 3.6.1.1) and thus $ef=n$ (Prop 3.6.2.4, (iii) implies (ii)). Note that if you weaken the hypotheses too much then there are counterexamples; it's possible to have $ef\lt n$ and BGR goes into details.

## Lean

Stated as [`IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 266](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L266)
