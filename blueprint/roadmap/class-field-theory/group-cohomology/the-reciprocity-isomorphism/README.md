# The Reciprocity Isomorphism

- [fundamental class](def-fundamental-class.md)

In this section we'll show that if $(R,G,M)$ is a finite class formation then there is an isomorphism (called the *reciprocity isomorphism*)

$$
\mathrm{reciprocity}: G^{\mathrm{ab}} \otimes R \cong H^0_{\mathrm{Tate}}(G,M).
$$

The reciprocity isomorphism depends on the choice of a fundamental class. In our application to local class field theory we will isolate a “canonical” fundamental class, called “the” fundamental class.

**Remark.**

- Given $G$ and $R$, there can be several nonisomorphic $M$ which are finite class formations. For example if $M$ is a finite class formation then so is $M\oplus N$ where $N$ is any cohomologically trivial module.
- I know of no example in class field theory where $R$ is any ring other than ${\mathbb Z}$.

**Example.** If $G$ is a finite cyclic group then the trivial representation ${\mathbb Z}$ (or more precisely the triple $({\mathbb Z},G,{\mathbb Z})$) is a finite class formation. This follows from [H2 cyclic Z](../periodicity-for-finite-cyclic-groups/lem-h2-cyclic-z.md). The cocycle $\sigma_G$ defined in [local inv iso](../periodicity-for-finite-cyclic-groups/lem-local-inv-iso.md) (which depends on a choice of generator for $G$) is a fundamental class. Note that it is unsurprising that the cocycle depends on a choice of generator, as the reciprocity isomorphism gives an isomorphism $G\cong {\mathbb Z}/|G|{\mathbb Z}.$

**Remark.** In the case $R={\mathbb Z}$ and $I\not=0$, which is the only case we shall use in applications, the lemma can just be proved by counting.

**Remark.** Again when $R={\mathbb Z}$ the above proof can be made much simpler.

We issue a warning: the previous lemma shows that the restriction of a fundamental class to a subgroup is a fundamental class. Later on we shall be talking about *the* fundamental class in local class field theory, as opposed to *a* fundamental class, and lemma [restriction fundamental class generates](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L2060) will not be good enough; we will need to check that *the* fundamental class restricts to *the* fundamental class.

Say $(R,G,M)$ is a finite class formation. We now begin the construction of the reciprocity isomorphism $G^{\mathrm{ab}}\otimes R\cong H^0_{\mathrm{Tate}}(G,M)$ from a fundamental class.

We next prove a formula for the reciprocity isomorphism in terms of a cocycle $\sigma'$ representing the fundamental class $\sigma$.
