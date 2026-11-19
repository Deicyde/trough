---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.encObs, MIPRE.Tailored.encObs_mul_self, MIPRE.Tailored.commute_encObs, MIPRE.Tailored.star_encObs, MIPRE.Tailored.fourierFactor_encObs, MIPRE.Tailored.fourierProj_encObs, MIPRE.Tailored.commute_encObs_encObs, MIPRE.Tailored.encObs_merge, MIPRE.Tailored.encObs_extend
statement: formalized
proof: formalized
---

# The bit observables of an encoded measurement

Let $(P_\lambda)_{\lambda \in \Lambda}$ be a projective measurement and $\mathrm{enc}$ a map from $\Lambda$ to $\mathbb{F}_2^k$. The observables $U_i = \sum_\lambda (-1)^{\mathrm{enc}(\lambda)_i} P_\lambda$ are commuting self-adjoint involutions, and their Fourier transform is the push-forward of $P$ along $\mathrm{enc}$: $\prod_i \frac12(1 + (-1)^{a_i} U_i) = \sum_{\mathrm{enc}(\lambda) = a} P_\lambda$. If every element of $P$ commutes with every element of a second projective measurement $Q$, the bit observables of $P$ commute with those of $Q$, whatever the encodings. Merging the outcomes of $P$ along a map $f$ and then encoding by $\mathrm{enc}$ gives the bit observables of $P$ along $\mathrm{enc} \circ f$, and so does extending the outcome set of $P$ by zero along an injection $f$.

## Depends on

- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](../part-01/def-fourier-forms.md)

## Proof

The map $\varepsilon \mapsto \sum_\lambda \varepsilon(\lambda) P_\lambda$ is multiplicative, so the $U_i$ are commuting involutions, self-adjoint as their weights are real. Since $\sum_\lambda P_\lambda = {I}$, the factor $\frac12(1 + (-1)^{b} U_i)$ is $\sum_\lambda \frac12(1 + (-1)^{b + \mathrm{enc}(\lambda)_i}) P_\lambda$, the coarse-graining of $P$ onto $\{\mathrm{enc}(\lambda)_i = b\}$; by multiplicativity the product over $i$ is the coarse-graining onto the intersection of these sets, by induction on $k$. The last two claims regroup the sum $\sum_\lambda$ by the fibres of $f$, resp. drop the outcomes outside the image of $f$, which carry zero.

## Lean

Formalized as [`MIPRE.Tailored.encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs), [`MIPRE.Tailored.encObs_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_mul_self), [`MIPRE.Tailored.commute_encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.commute_encObs), [`MIPRE.Tailored.star_encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.star_encObs), [`MIPRE.Tailored.fourierFactor_encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierFactor_encObs), [`MIPRE.Tailored.fourierProj_encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierProj_encObs), [`MIPRE.Tailored.commute_encObs_encObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.commute_encObs_encObs), [`MIPRE.Tailored.encObs_merge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_merge), [`MIPRE.Tailored.encObs_extend`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_extend).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1344](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1344)
