# Examples

We discuss some examples of Haar characters.

- [MeasureTheory.ringHaarChar_real](measuretheory-ringhaarchar-real.md)
- [MeasureTheory.ringHaarChar_complex](measuretheory-ringhaarchar-complex.md)
- [MeasureTheory.ringHaarChar_padic](measuretheory-ringhaarchar-padic.md)

**Remark.** If $R$ is a finite extension of $\mathbb{Q}_p$ then $\delta_R(u)$ is the norm on $R$ normalised in the following way: $\delta_R(\varpi)=q^{-1}$, where $\varpi$ is a uniformiser and $q$ is the size of the (finite) residue field. In fact the same is true for any nonarchimedean local field. The proof is the same as for $\mathbb{Q}_p$. Right now this is difficult to state in Lean because there is still some discussion about the definition of a nonarchimedean local field.
