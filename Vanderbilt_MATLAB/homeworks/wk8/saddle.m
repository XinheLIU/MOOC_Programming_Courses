function indices = saddle(M)
 %saddle point is defined as an element whose value is greater than or equal to every element in its row
 %and less than or equal to every element in its column
 indices=[]
 for j=1:size(M,2)
      for i=1:size(M,1)
          if M(i,j)==min(M(:,j)) && M(i,j)==max(M(i,:))
            indices=[indices;i j]
          end
      end
 end
 
