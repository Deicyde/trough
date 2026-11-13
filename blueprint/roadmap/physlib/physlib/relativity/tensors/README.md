# Tensors

The folder [Physlib/Relativity/Tensors/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors): 67 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Tensors* ([Physlib/Relativity/Tensors/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Tensor species
>
> A tensor species consists of a symmetry group, a type of index colors, a representation and a basis for each color, an involution sending each color to the dual color it may contract with, and contraction and unit data satisfying coherence conditions. [\[1\]](part-04/tensorspecies-basic.md) A species may carry a metric: an invariant tensor for each color whose contraction against the metric of the dual color is the unit, this condition forming a class of its own. [\[2\]](part-04/tensorspecies-basic.md) …
>
> ### Tensors and their components
>
> Given a species and a list of colors, the tensors with those indices form the tensor product of the color representations over the index set, and the pure tensors are the choices of one vector for each index. [\[3\]](part-01/basic.md) A component label assigns a basis index to each tensor index. [\[4\]](part-02/componentidx-basic.md) A component label of a single index is a basis index of its color, a label of a concatenated index list is a pair of labels, and a label drops a contracted pair of indices. [\[5\]](part-02/componentidx-single.md)[\[6\]](part-02/componentidx-product.md)[\[7\]](part-02/componentidx-contraction.md) A tensor corresponds to its components in the component basis, and the tensors with no indices are the scalars. [\[3\]](part-01/basic.md)
>
> ### Group action and reindexing
>
> The symmetry group acts on pure tensors and on tensors. [\[8\]](part-01/basic.md) Indices permute along a color-preserving map, equivariantly, functorially and injectively. [\[8\]](part-01/basic.md) The maps that count as reindexings are characterized and are closed under inverse and composition; they include the index maps used by products, evaluation and contraction. [\[9\]](part-01/reindexing.md)
>
> ### Products
>
> The tensor product of two pure tensors, or of two tensors, concatenates their index lists. [\[10\]](part-01/product.md) It has explicit components in the basis, is equivariant, and is compatible with swapping the factors, permuting either factor, and rebracketing. [\[10\]](part-01/product.md)
>
> ### Contraction
>
> A pair of indices of dual color contracts, on pure tensors and on tensors, deleting the pair from the index list. [\[11\]](part-03/contraction-succsuccabove.md)[\[12\]](part-02/contraction-pure.md)[\[13\]](part-02/contraction-basic.md) Contraction is equivariant, commutes with permutations, is symmetric in the contracted pair, and contractions of two different pairs commute. [\[13\]](part-02/contraction-basic.md) Its components in the basis are sums over the contracted label. [\[14\]](part-02/contraction-basis.md) Contracting inside one factor of a product agrees with contracting the product. [\[15\]](part-02/contraction-products.md)
>
> One tensor also contracts against another at an addressed slot, either with the result placed at the end [\[16\]](part-02/contraction-crosstoend.md) or with the result placed at the slot. [\[17\]](part-02/contraction-crosstoslot.md) For real Lorentz tensors the result-to-end contraction has explicit components in the standard basis. [\[18\]](part-03/realtensor-contraction-crosstoend.md)
>
> ### Units, metrics, raising and lowering
>
> The unit tensor of a color is invariant under the group action, has explicit components, and is the permuted unit tensor of the dual color. [\[19\]](part-01/unittensor.md) The metric tensor of a color is invariant, and contracting it against the metric tensor of the dual color gives the unit. [\[20\]](part-01/metrictensor.md) The unit tensor is an identity for contraction at a slot, so raising and then lowering an index is a round trip. [\[21\]](part-03/contraction-unittensorcontraction.md) Raising or lowering a named index, by contraction with the metric, is an equivariant linear equivalence. [\[22\]](part-01/dual.md)
>
> ### Evaluation
>
> One index of a tensor evaluates at a fixed basis label, on pure tensors and on tensors. [\[23\]](part-01/evaluation.md) Evaluation has explicit components in the basis, and commutes with permutations, with other evaluations, with contractions and with products in their right factor. [\[23\]](part-01/evaluation.md) A tensor is the sum over basis labels of the evaluations of its last index, each tensored with the matching rank-one basis tensor and permuted back into the last slot. [\[23\]](part-01/evaluation.md) …
>
> ### Constructing tensors
>
> Tensors arise from single vectors, from elements of a tensor product of two or three carriers, and from invariant maps. [\[24\]](part-01/constructors.md) They also arise from integer components in the standard basis. [\[25\]](part-01/ofint.md) Complex Lorentz tensors arise from Gaussian-integer components, compatibly with products, contractions and permutations. [\[26\]](part-01/complextensor-ofgaussianint.md)
>
> ### Index notation
>
> An elaborator turns pen-and-paper index expressions into tensor operations. [\[27\]](part-01/elab.md) The design follows Tooby-Smith \{1}. A class carries index notation to any type linearly equivalent to a tensor, with the induced group action, basis and products. [\[28\]](part-01/tensorial.md)
>
> ### Conjugation
>
> A species may carry a conjugation: a second involution on colors together with a conjugation of tensors, which is involutive and commutes with contraction. [\[29\]](part-02/conjugation-basic.md) A componentwise criterion for a tensor to equal a permutation of its conjugate expresses reality, and gives the Hermitian condition on a metric slot. [\[29\]](part-02/conjugation-basic.md) …
>
> ### Real Lorentz tensors
>
> The real Lorentz tensors form a species over the Lorentz group \{2} with an upper and a lower color, each dual to the other; in it, contraction is a sum of evaluations. [\[30\]](part-03/realtensor-basic.md) Its colors are carried by the contravariant and covariant modules, with their representations of the Lorentz group and their standard bases. [\[31\]](part-04/realtensor-vector-pre-modules.md)[\[32\]](part-04/realtensor-vector-pre-basic.md) The two modules contract invariantly against each other. [\[33\]](part-04/realtensor-vector-pre-contraction.md) The species has metric maps [\[34\]](part-03/realtensor-metrics-pre.md) and unit maps. [\[35\]](part-03/realtensor-units-pre.md) Its metric tensors have the Minkowski matrix as components in the standard basis, and raising or lowering an index multiplies components by the Minkowski matrix. [\[36\]](part-03/realtensor-metrics-basic.md) Its unit tensor has explicit components. [\[37\]](part-03/realtensor-units-basic.md) Pairwise tensor products of the two modules are square matrices. [\[38\]](part-03/realtensor-matrix-pre.md) …
>
> ### Lorentz vectors and covectors
>
> A Lorentz vector is a function on one time index and d space indices. [\[39\]](part-03/realtensor-vector-basic.md) Lorentz vectors carry module, norm and inner-product structures, a charted-space structure, a standard basis and coordinate maps, a time component and a spatial part, and a model with corners under which they form a manifold. [\[39\]](part-03/realtensor-vector-basic.md) The Lorentz group acts on them by matrix-vector multiplication. [\[40\]](part-03/realtensor-vector-representation.md) They are tensorial, the induced action on the standard basis being the matrix action. [\[41\]](part-04/realtensor-vector-tensorial.md) Lorentz covectors carry the same structures [\[42\]](part-03/realtensor-covector-basic.md) , the same kind of representation [\[43\]](part-03/realtensor-covector-representation.md) , and a tensorial instance. [\[44\]](part-03/realtensor-covector-tensorial.md) Vectors and covectors contract invariantly against each other. [\[45\]](part-03/realtensor-representation-contraction.md)
>
> ### Minkowski product and causality
>
> The Minkowski product of two Lorentz vectors is symmetric, Lorentz invariant and nondegenerate. [\[46\]](part-03/realtensor-vector-minkowskiproduct.md) Linear maps have adjoints with respect to it, and a linear map preserves it exactly when its matrix lies in the Lorentz group. [\[46\]](part-03/realtensor-vector-minkowskiproduct.md)
>
> Each vector has a causal character — timelike, lightlike or spacelike — that is invariant under Lorentz transformations, and the product determines light cones, causal precedence and causal diamonds. [\[47\]](../causality/basic.md) A vector is spacelike exactly when its Minkowski norm squared is negative. [\[47\]](../causality/basic.md) It is timelike exactly when that norm squared is positive, and then its time component dominates its spatial part. [\[48\]](../causality/timelike.md) It is lightlike exactly when that norm squared vanishes, and causal precedence is reflexive. [\[49\]](../causality/lightlike.md) A Lorentz velocity is a future-directed vector of unit Minkowski norm; its time component is positive and dominates its spatial part, and the velocities form a path-connected set. [\[50\]](part-04/realtensor-velocity-basic.md)
>
> ### Levi-Civita tensor
>
> The rank-four Levi-Civita tensor is a real Lorentz tensor in three spatial dimensions whose components in the standard basis are the Levi-Civita symbol, and it is antisymmetric under each adjacent transposition of indices. [\[51\]](part-03/levicivita-basic.md) The Euclidean Levi-Civita symbol satisfies the epsilon-epsilon contraction identities summed over all four index slots, over the last three, and over the last two. [\[52\]](part-03/levicivita-contractions.md) At the level of tensors, contracting the Levi-Civita tensor with itself over all four index pairs gives −24, and over the first three gives −6 times the unit tensor of the lower color. [\[63\]](part-03/levicivita-contractions.md)[\[64\]](part-03/realtensor-metrics-basic.md)[\[37\]](part-03/realtensor-units-basic.md) …
>
> ### Complex Lorentz tensors
>
> The complex Lorentz tensors form a species over SL(2, ℂ) with the left- and right-handed Weyl colors \{3}, their duals, and the two Lorentz vector colors. [\[53\]](part-01/complextensor-basic.md) The vector colors are carried by complex contravariant and covariant modules with their representations of SL(2, ℂ), which contract invariantly against each other. [\[54\]](part-02/complextensor-vector-modules.md)[\[55\]](part-02/complextensor-vector-contraction.md) The metric tensors [\[56\]](part-01/complextensor-metrics-basic.md) and unit tensors [\[57\]](part-01/complextensor-units-basic.md) of each color have several equivalent forms, including Gaussian-integer components, and the units are symmetric. [\[58\]](part-02/complextensor-units-symm.md) Pairwise products of complex Lorentz vectors are square matrices. [\[59\]](part-01/complextensor-matrix-pre.md) The full contraction of an antisymmetric tensor with a symmetric one equals its own negative. [\[60\]](part-01/complextensor-lemmas.md) The complex Levi-Civita tensor has Gaussian-integer components. [\[61\]](part-03/levicivita-complex.md)
>
> ### From real to complex tensors
>
> A canonical injective semilinear map takes real Lorentz tensors to complex ones, sending colors and component labels to their complex counterparts. [\[62\]](part-03/realtensor-tocomplex.md) It is equivariant for the complexified Lorentz group and commutes with permutations, products, contractions and evaluations of indices. [\[62\]](part-03/realtensor-tocomplex.md)

Its references:

> - \{1\} J. Tooby-Smith, *Formalization of physics index notation in Lean 4*, arXiv:2411.07667, https://arxiv.org/abs/2411.07667
> - \{2\} Lorentz Group API map — [Physlib/Relativity/LorentzGroup/API-map.md](../lorentzgroup/README.md)
> - \{3\} Weyl Fermions API map — [Physlib/Relativity/Fermions/Weyl/API-map.md](../fermions/weyl/README.md)

## [Tensors to Physlib.Relativity.Tensors.Compl…](part-01/README.md)

- [Tensors](part-01/basic.md)
- [Constructors of tensors.](part-01/constructors.md)
- [Dual tensors](part-01/dual.md)
- [Elaboration of tensor expressions](part-01/elab.md)
- [Evaluation of tensor indices](part-01/evaluation.md)
- [The metric tensors](part-01/metrictensor.md)
- [Basis for tensors in a tensor species](part-01/ofint.md)
- [The product of tensors](part-01/product.md)
- [Reindexing of tensor components](part-01/reindexing.md)
- [Tensorial class](part-01/tensorial.md)
- [The unit tensors](part-01/unittensor.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Basic](part-01/complextensor-basic.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Lemmas](part-01/complextensor-lemmas.md)
- [Complex Lorentz tensors with Gaussian integer components](part-01/complextensor-ofgaussianint.md)
- [Tensor products of two complex Lorentz vectors](part-01/complextensor-matrix-pre.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](part-01/complextensor-metrics-basic.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Lemmas](part-01/complextensor-metrics-lemmas.md)
- [Metric for complex Lorentz vectors](part-01/complextensor-metrics-pre.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Units.Basic](part-01/complextensor-units-basic.md)

## [Unit for complex Lorentz… to The bilinear map and the…](part-02/README.md)

- [Unit for complex Lorentz vectors (ComplexTensor/Units/Pre)](part-02/complextensor-units-pre.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Units.Symm](part-02/complextensor-units-symm.md)
- [Complex Lorentz vectors](part-02/complextensor-vector-basic.md)
- [Contraction of Lorentz vectors](part-02/complextensor-vector-contraction.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Vector.Modules](part-02/complextensor-vector-modules.md)
- [Component indices](part-02/componentidx-basic.md)
- [Contractions of component indices](part-02/componentidx-contraction.md)
- [Component indices split at a single slot](part-02/componentidx-insert.md)
- [Component indices for two-index tensors](part-02/componentidx-pair.md)
- [Products of component indices](part-02/componentidx-product.md)
- [Component indices for one-index tensors](part-02/componentidx-single.md)
- [Conjugation structure on a tensor species](part-02/conjugation-basic.md)
- [The inverse of a rank-two tensor](part-02/conjugation-inverse.md)
- [Contractions on tensors](part-02/contraction-basic.md)
- [Contractions on basis tensors](part-02/contraction-basis.md)
- [Cross contraction at named slots](part-02/contraction-crosstoend.md)
- [Result-to-slot contraction against a rank-2 tensor](part-02/contraction-crosstoslot.md)
- [The interaction of contractions and products](part-02/contraction-products.md)
- [Contractions on pure tensors](part-02/contraction-pure.md)
- [The bilinear map and the product of rank-two tensors](part-02/contraction-ranktwo.md)

## [Defining succSuccAbove to Representation of the Lorentz…](part-03/README.md)

- [Defining succSuccAbove](part-03/contraction-succsuccabove.md)
- [Contraction against the unit tensor](part-03/contraction-unittensorcontraction.md)
- [The Levi-Civita tensor as a real Lorentz tensor](part-03/levicivita-basic.md)
- [The Levi-Civita tensor as a complex Lorentz tensor](part-03/levicivita-complex.md)
- [Contraction identities for the Levi-Civita tensor](part-03/levicivita-contractions.md)
- [Physlib.Relativity.Tensors.RealTensor.Basic](part-03/realtensor-basic.md)
- [Complex Lorentz tensors from real Lorentz tensors](part-03/realtensor-tocomplex.md)
- [Components of real Lorentz cross contractions](part-03/realtensor-contraction-crosstoend.md)
- [Lorentz co vectors](part-03/realtensor-covector-basic.md)
- [Representation of the Lorentz group on Lorentz vectors (CoVector/Representation)](part-03/realtensor-covector-representation.md)
- [Tensorial nature of Lorentz covectors](part-03/realtensor-covector-tensorial.md)
- [Tensor products of two real Lorentz vectors](part-03/realtensor-matrix-pre.md)
- [Physlib.Relativity.Tensors.RealTensor.Metrics.Basic](part-03/realtensor-metrics-basic.md)
- [Metric for real Lorentz vectors](part-03/realtensor-metrics-pre.md)
- [Contraction of Real Lorentz Vectors and Covectors](part-03/realtensor-representation-contraction.md)
- [Unit tensors for real Lorentz tensors](part-03/realtensor-units-basic.md)
- [Unit for complex Lorentz vectors (RealTensor/Units/Pre)](part-03/realtensor-units-pre.md)
- [Lorentz Vectors](part-03/realtensor-vector-basic.md)
- [Minkowski product on Lorentz vectors](part-03/realtensor-vector-minkowskiproduct.md)
- [Representation of the Lorentz group on Lorentz vectors (Vector/Representation)](part-03/realtensor-vector-representation.md)

## [Tensorial nature of Lorentz… to Species whose bases at dual…](part-04/README.md)

- [Tensorial nature of Lorentz vectors](part-04/realtensor-vector-tensorial.md)
- [Real Lorentz vectors](part-04/realtensor-vector-pre-basic.md)
- [Contraction of Real Lorentz vectors](part-04/realtensor-vector-pre-contraction.md)
- [Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Modules](part-04/realtensor-vector-pre-modules.md)
- [Lorentz Velocities](part-04/realtensor-velocity-basic.md)
- [Derivatives of Lorentz velocities](part-04/realtensor-velocity-deriv.md)
- [Tensor species (Basic)](part-04/tensorspecies-basic.md)
- [Species whose bases at dual colors are dual bases](part-04/tensorspecies-dualbasis.md)
