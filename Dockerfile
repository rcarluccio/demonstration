FROM underworldcode/uw2cylindrical:cylindrical

# Set the UW_MACHINE env variable for metrics
ENV UW_MACHINE binder
RUN git clone https://github.com/rsbyrne/demonstration.git
