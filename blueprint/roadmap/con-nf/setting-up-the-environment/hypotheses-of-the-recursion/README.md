# Hypotheses of the recursion

- [model data](def-modeldata.md)
- [tangle](def-tangle.md)
- [fuzz maps](prop-fuzz.md)
- [inflexible path](def-inflexiblepath.md)
- [typed near-litter](def-typednearlitter.md)
- [coherent data](def-coherentdata.md)

The strategy of our construction is as follows.

- In [Constructing the types](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/content.tex#L9), we assume model data, position functions, and typed near-litters for all types $\beta < \alpha$, and construct model data at level $\alpha$.
- In [Freedom of action](../../freedom-of-action/README.md) and [The counting argument](../../the-counting-argument/README.md), we assume coherent data below level $\alpha$ (along with the assumptions required for this definition to make sense) and prove that $\#\mathsf{TSet}_\alpha = \#\mu$.
- In [Wrapping up the main induction](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/content.tex#L21), we use the results of [Constructing the types](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/content.tex#L9), [Freedom of action](../../freedom-of-action/README.md) and [The counting argument](../../the-counting-argument/README.md) to show that we can provide position functions and typed near-litters at level $\alpha$. We then show that these constructions may be iterated so that we may define all of the above structures at every proper type level.
