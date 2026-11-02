---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.range_baseChange_comp_tensorAdicCompletionTo_eq_pi
statement: formalized
proof: formalized
---

# IsDedekindDomain.HeightOneSpectrum.range\_baseChange\_comp\_tensorAdicCompletionTo\_eq\_pi

The isomorphism $L\otimes_KK_v\to\prod_{w|v}L_w$ induces an isomorphism $B\otimes_AA_v\to \prod_{w|v}B_w$ for all $v$ in the height one spectrum of $A$.

## Depends on

- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv](isdedekinddomain-heightonespectrum-adiccompletio-3.md)

## Proof

Certainly the image of the integral elements are integral. The argument in the other direction is more delicate. My original plan was to follow Cassels–Froehlich, Cassels' article “Global fields”, section 12 lemma, p61, which proves it for all but finitely many primes, but [a PR by Matthew Jasper](https://github.com/ImperialCollegeLondon/FLT/pull/400) gives another approach which works for all primes. Jasper's argument is to show that the closure of $A$ in $K_v$ is $A_v$ for a valuation on a Dedekind domain, and then that the closure of $A$ in $\prod_{v\in S}K_v$ is $\prod_{v\in S}A_v$ for $S$ a finite set of valuations (using the Chinese remainder theorem). Applying this to $B$ we get that the closure of $B$ in $\prod_{w|v}L_w$ is $\prod_{w|v}B_w$. He then shows that this closure is the image of $B\otimes_A\mathcal{O}_v$ (by showing that this image is closed because it's open), giving surjectivity; injectivity follows from the statement that $L\otimes_KK_v=\prod_{w|v}L_w$.

## Lean

Formalized as [`IsDedekindDomain.HeightOneSpectrum.range_baseChange_comp_tensorAdicCompletionTo_eq_pi`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.HeightOneSpectrum.range_baseChange_comp_tensorAdicCompletionTo_eq_pi).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 331](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L331)
