# STIR

## Tools for Reed Solomon codes

### Random linear combination as a proximity generator

- [proximity_gap](thm-proximity-gap.md)

### Univariate Function Quotienting

In the following, we start by defining the *quotient* of a univariate function.

- [quotient](def-quotient.md)

Next we define the polynomial quotient operator, which quotients a polynomial relative to its output on evaluation points. The polynomial quotient is a polynomial of lower degree.

- [poly_quotient](def-poly-quotient.md)

The following lemma, implicit in prior works, shows that if the function is “quotiented by the wrong value”, then its quotient is far from low-degree.

- [quotienting](lemma-quotienting.md)

### Out of domain sampling

- [out_of_domain_smpl](lemma-out-of-domain-smpl.md)

### Folding univariate functions

STIR relies on $k$-wise folding of functions and polynomials - this is similar to prior works, although presented in a slightly different form. As shown below, folding a function preserves proximity from the Reed-Solomon code with high probability. The folding operator is based on the following fact, decomposing univariate polynomials into bivariate ones.

- [poly_folding](fact-poly-folding.md)

Moreover, $\hat{Q}$ can be computed efficiently given $\hat{f}$ and $\hat{q}$; the formalization defines it by repeated division by $\hat{q}$.

Below, we define folding of a polynomial followed by folding of a function.

- [poly_folding](def-poly-folding.md)
- [fn_folding](def-fn-folding.md)

The following lemma shows that the distance of a function is preserved under folding. If a functions $f$ has distance $\delta$ to a Reed-Solomon code then, with high probability over the choice of folding randomness, its folding also has a distance of $\delta$ to the “$k$-wise folded” Reed-Solomon code.

- [folding](lemma-folding.md)

### Combine functions of varying degrees

We show a new method for combining functions of varying degrees with minimal proximity require- ments using geometric sums. We begin by recalling a fact about geometric sums.

- [geometric_sum](fact-geometric-sum.md)
- [combine](def-combine.md)
- [deg_corr](def-deg-corr.md)

Below it is shown that combining multiple polynomials of varying degrees can be done as long as the proximity error is bounded by $(\min{\{1-{\mathsf{B}}^*(\rho),1-\rho-1/|\mathcal{L}|\}})$.

- [combine](lemma-combine.md)
